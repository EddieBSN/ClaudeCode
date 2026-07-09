"""Builds the argparse parser from a declarative command table."""

import argparse
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Tuple

Handler = Callable[[argparse.Namespace], str]


@dataclass(frozen=True)
class Argument:
    """One argparse argument: positional name or option flags, plus options."""

    flags: Tuple[str, ...]
    options: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Command:
    """One subcommand: its name, help text, handler, and arguments."""

    name: str
    help: str
    handler: Handler
    arguments: Tuple[Argument, ...] = ()


def build_parser(commands: Tuple[Command, ...]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tasks", description="Task CRUD manager")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in commands:
        _register(subparsers, command)
    return parser


def _register(subparsers, command: Command) -> None:
    subparser = subparsers.add_parser(command.name, help=command.help)
    for argument in command.arguments:
        subparser.add_argument(*argument.flags, **argument.options)
    subparser.set_defaults(handler=command.handler)
