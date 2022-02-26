"""
:author: Doug Skrypa
"""

from shutil import get_terminal_size
from textwrap import TextWrapper
from typing import TYPE_CHECKING, Optional

from .utils import ProgramMetadata, Bool

if TYPE_CHECKING:
    from .commands import CommandType
    from .command_parameters import CommandParameters
    from .parameters import ParamGroup, Parameter


class HelpFormatter:
    def __init__(self, command: 'CommandType', params: 'CommandParameters'):
        from .parameters import ParamGroup  # here due to circular dependency

        self.command = command
        self.params = params
        self.pos_group = ParamGroup(description='Positional arguments')
        self.opt_group = ParamGroup(description='Optional arguments')
        self.groups = [self.pos_group, self.opt_group]

    def maybe_add_group(self, *groups: 'ParamGroup'):
        for group in groups:
            if group.contains_positional:
                self.pos_group.add(group)
            else:
                self.groups.append(group)

    def maybe_add_param(self, *params: 'Parameter'):
        for param in params:
            if not param.group:
                if param._positional:
                    self.pos_group.add(param)
                else:
                    self.opt_group.add(param)

    # def maybe_add(self, *params: ParamOrGroup):
    #     for param in params:
    #         if isinstance(param, ParamGroup):
    #             if any(isinstance(p, BasePositional) for p in param):
    #                 self.pos_group.add(param)
    #             else:
    #                 self.groups.append(param)
    #         elif not param.group:
    #             if isinstance(param, BasePositional):
    #                 self.pos_group.add(param)
    #             else:
    #                 self.opt_group.add(param)

    def format_usage(self, delim: str = ' ') -> str:
        meta: ProgramMetadata = self.command._Command__meta
        if usage := meta.usage:
            return usage

        params = self.params.positionals + self.params.options  # noqa
        if (pass_thru := self.params.pass_thru) is not None:  # noqa
            params.append(pass_thru)

        parts = ['usage:', meta.prog]
        parts.extend(param.format_basic_usage() for param in params if param.show_in_help)
        return delim.join(parts)

    def format_help(
        self, width: int = 30, add_default: Bool = True, group_type: Bool = True, extended_epilog: Bool = True
    ):
        meta: ProgramMetadata = self.command._Command__meta
        parts = [self.format_usage(), '']
        if description := meta.description:
            parts += [description, '']

        for group in self.groups:
            if group.show_in_help:
                parts.append(group.format_help(width=width, add_default=add_default, group_type=group_type))

        if epilog := meta.format_epilog(extended_epilog):
            parts.append(epilog)

        return '\n'.join(parts)


class HelpEntryFormatter:
    def __init__(self, usage: str, description: Optional[str], width: int = 30, lpad: int = 2):
        self.usage = usage
        self.width = width
        self.lines = []
        self.term_width = get_terminal_size()[0]
        self.process_usage(usage, lpad)
        if description:
            self.process_description(description)

    def process_usage(self, usage: str, lpad: int = 2):
        if len(usage) + lpad > self.term_width:
            tw = TextWrapper(
                self.term_width,
                initial_indent=' ' * lpad,
                subsequent_indent=' ' * self.width,
                # drop_whitespace=False,
                # replace_whitespace=False,
                # expand_tabs=False,
            )
            # prefix = ' ' * self.width
            # for i, line in enumerate(tw.wrap(usage)):
            #     self.lines.append(f'{prefix}{line.lstrip()}')

            self.lines.extend(tw.wrap(usage))
        else:
            left_pad = ' ' * lpad
            self.lines.append(left_pad + usage)

    def process_description(self, description: str):
        full_indent = ' ' * self.width
        line = self.lines[0]
        if (pad_chars := self.width - len(line)) < 0 or len(self.lines) != 1:
            if len(description) + self.width < self.term_width:
                self.lines.append(full_indent + description)
            else:
                tw = TextWrapper(self.term_width, initial_indent=full_indent, subsequent_indent=full_indent)
                self.lines.extend(tw.wrap(description))
        else:
            mid = ' ' * pad_chars
            line += mid + description
            if len(line) > self.term_width:
                tw = TextWrapper(self.term_width, initial_indent='', subsequent_indent=full_indent)
                self.lines = tw.wrap(line)
            else:
                self.lines = [line]

    def __call__(self):
        return '\n'.join(self.lines)
