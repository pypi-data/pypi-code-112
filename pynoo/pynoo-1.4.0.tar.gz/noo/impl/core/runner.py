from __future__ import annotations

from pathlib import Path

from typer import echo

from ..models import CreateAction, DeleteAction, RenameAction, ReplaceAction, Step
from .formatter import format_vars, replace

OPMAP = {
    "eq": lambda a, b: str(a) == str(b),
    "ne": lambda a, b: str(a) != str(b),
    "gt": lambda a, b: int(a) > int(b),
    "ge": lambda a, b: int(a) >= int(b),
    "lt": lambda a, b: int(a) < int(b),
    "le": lambda a, b: int(a) <= int(b),
}


class Runner:
    def __init__(self, base: Path, steps: list[Step], variables: dict[str, dict[str, str | int]]) -> None:
        self.base = base
        self.steps = steps
        self.vars = variables

    def _resolve_var(self, var: str) -> str | int:
        ns, name = var.removeprefix("$$").split(":", 1)

        if ns not in ("noo", "var"):
            raise ValueError(f"Unknown namespace: {ns}")

        if name not in self.vars[ns]:
            raise ValueError(f"Unknown variable: {ns}:{name}")

        return self.vars[ns][name]

    def _run_replace(self, files: list[str], src: str, dest: str) -> None:
        for file in files:
            path = self.base / file

            source = path.read_text()
            target = replace(source, src, dest, self.vars)
            path.write_text(target)

    def _run_delete(self, files: list[str]) -> None:
        for file in files:
            path = self.base / file

            if path.exists():
                path.unlink()

    def _run_create(self, file: str, content: str) -> None:
        path = self.base / file
        path.write_text(format_vars(content, self.vars))

    def _run_rename(self, file: str, dest: str) -> None:
        path = self.base / file

        if not path.exists():
            raise ValueError(f"No such file: {path}")

        path.rename(self.base / dest)

    def _verify_step_conditions(self, step: Step) -> bool:
        if step.conditions is None:
            return True

        for condition in step.conditions:
            var = self._resolve_var(condition.var)
            value = condition.value

            op = OPMAP[condition.op]

            if not op(var, value):
                return False

        return True

    def _run_step(self, step: Step) -> None:
        if not self._verify_step_conditions(step):
            echo(f"Skipping step {step.name}.")
            return

        for action in step.actions:
            if isinstance(action, ReplaceAction):
                self._run_replace(action.files, action.src, action.dest)
            elif isinstance(action, DeleteAction):
                self._run_delete(action.files)
            elif isinstance(action, CreateAction):
                self._run_create(action.file, action.content or "")
            elif isinstance(action, RenameAction):
                self._run_rename(action.file, action.dest)
            else:
                raise ValueError(f"Invalid action: {action}")

    def run(self) -> None:
        for step in self.steps:
            echo(f"Running step {step.name}.")

            self._run_step(step)
