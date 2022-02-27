
from __future__ import annotations

import argparse
import dataclasses
import logging
import typing as t
from pathlib import Path

from novella.action import Action

if t.TYPE_CHECKING:
  from nr.util.digraph import DiGraph
  from nr.util.inspect import Callsite
  from novella.template import Template

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Option:
  long_name: str | None
  short_name: str | None
  description: str | None
  flag: bool
  default: str | bool | None


class Novella:
  """ This class is the main entrypoint for starting and controlling a Novella build. """

  BUILD_FILE = Path('build.novella')

  def __init__(self, project_directory: Path) -> None:
    self.project_directory = project_directory

  def execute_file(self, file: Path | None = None) -> NovellaContext:
    """ Execute a file, allowing it to populate the Novella pipeline. """

    from craftr.dsl import Closure
    context = NovellaContext(self)
    file = file or self.BUILD_FILE
    Closure(None, None, context).run_code(file.read_text(), str(file))
    return context


class NovellaContext:
  """ The Novella context contains the action pipeline and all the data collected during the build script execution. """

  def __init__(self, novella: Novella) -> None:
    self._novella = novella
    self._init_sequence: bool = True

    self._actions: dict[str, Action] = {}
    self._last_action_added: Action | None = None
    self._fallback_dependencies: dict[Action, Action] = {}
    self._action_configurators: list[tuple[Action, t.Callable]] = []

    self._options: dict[str, str | bool | None] = {}
    self._option_spec: list[Option] = []
    self._option_names: list[str] = []

  @property
  def novella(self) -> Novella:
    return self._novella

  @property
  def options(self) -> dict[str, str | bool | None]:
    return self._options

  @property
  def project_directory(self) -> Path:
    return self.novella.project_directory

  def option(
    self,
    long_name: str,
    short_name: str | None = None,
    description: str | None = None,
    flag: bool = False,
    default: str | bool | None = None,
  ) -> None:
    """ Add an option to the Novella pipeline that can be specified on the CLI. Actions can pick up the parsed
    option values from the #options mapping. """

    if len(long_name) == 1 and not short_name:
      long_name, short_name = '', long_name

    self._option_names.append(long_name)
    self._option_spec.append(Option(long_name, short_name, description, flag, default))

  def do(
    self,
    action_type_name: str,
    closure: t.Callable | None = None,
    name: str | None = None,
  ) -> None:
    """ Add an action to the Novella pipeline identified by the specified *action_type_name*. The action will be
    configured once it is created using the *closure*. """

    from nr.util.inspect import get_callsite
    from nr.util.plugins import load_entrypoint

    if name is None:
      name = action_type_name

    if name in self._actions:
      raise ValueError(f'action name {name!r} already used')

    action_cls = load_entrypoint(Action, action_type_name)  # type: ignore
    action = action_cls(self, name, get_callsite())
    self._actions[name] = action
    if closure is not None:
      if self._init_sequence:
        self._action_configurators.append((action, closure))
      else:
        closure(action)
    if self._last_action_added:
      self._fallback_dependencies[action] = self._last_action_added
    self._last_action_added = action

  def action(self, action_name: str, closure: t.Callable | None = None) -> Action:
    """ Access an action by its given name, and optionally apply the *closure*. """

    action = self._actions[action_name]
    if self._init_sequence and closure:
      self._action_configurators.append((action, closure))
    elif closure:
      closure(action)
    return action

  def template(self, template_name: str, init: t.Callable | None = None, post: t.Callable | None = None) -> None:
    """ Load a template and add it to the Novella pipeline. """

    from nr.util.plugins import load_entrypoint
    from novella.template import Template

    template_cls: type[Template] = load_entrypoint(Template, template_name)  # type: ignore
    template = template_cls()
    if init:
      init(template)
    template.define_pipeline(self)
    if post:
      post(template)

  def update_argument_parser(self, parser: argparse.ArgumentParser) -> None:
    group = parser.add_argument_group('script')
    for option in self._option_spec:
      option_names = []
      if option.long_name:
        option_names += [f"--{option.long_name}"]
      if option.short_name:
        option_names += [f"-{option.short_name}"]
      group.add_argument(
        *option_names,
        action="store_true" if option.flag else None,  # type: ignore
        help=option.description,
        default=option.default
      )

  def configure(self, args: list[str]) -> None:
    """ Parse the argument list and run the configuration for all registered actions. """

    if not self._init_sequence:
      raise RuntimeError('already configured')
    self._init_sequence = False

    parser = argparse.ArgumentParser()
    self.update_argument_parser(parser)
    parsed_args = parser.parse_args(args)
    for option_name in self._option_names:
      self.options[option_name] = getattr(parsed_args, option_name.replace('-', '_'))

    for action, closure in self._action_configurators:
      closure(action)
    self._action_configurators.clear()

  def get_actions_graph(self) -> DiGraph[str, Action, None]:
    from nr.util.digraph import DiGraph
    graph = DiGraph[str, Action, None]()
    for action_name, action in self._actions.items():
      assert action.name == action_name, (action, action_name)
      graph.add_node(action.name, action)
    for action in self._actions.values():
      if action.dependencies is None:
        if action in self._fallback_dependencies:
          action.dependencies = [self._fallback_dependencies[action]]
      for dep in action.dependencies or []:
        graph.add_edge(dep.name, action.name, None)
    return graph

  def get_actions_ordered(self) -> list[Action]:
    from nr.util.digraph.algorithm.topological_sort import topological_sort
    graph = self.get_actions_graph()
    return [self._actions[k] for k in topological_sort(graph)]


class PipelineError(Exception):

  def __init__(self, action_name: str, callsite: Callsite) -> None:
    self.action_name = action_name
    self.callsite = callsite
