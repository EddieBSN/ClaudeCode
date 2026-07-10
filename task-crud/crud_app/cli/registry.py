"""The declarative command table: data, not argparse call chains.

Adding a subcommand means adding one entry here and one handler method —
no parser-building code changes (open/closed at the CLI boundary).
"""

import argparse
from typing import Tuple

from crud_app.cli.commands import TaskCommands
from crud_app.cli.parser import Argument, Command

_ID = Argument(("id",), {"type": int})
_OPTIONAL_DONE = Argument(
    ("--done",), {"action": argparse.BooleanOptionalAction, "default": None}
)


def command_table(handlers: TaskCommands) -> Tuple[Command, ...]:
    return (
        Command(
            name="create",
            help="Create a task",
            handler=handlers.create,
            arguments=(
                Argument(("title",)),
                Argument(("-d", "--description"), {"default": ""}),
            ),
        ),
        Command(
            name="show",
            help="Show one task",
            handler=handlers.show,
            arguments=(_ID,),
        ),
        Command(
            name="list",
            help="List all tasks",
            handler=handlers.list,
        ),
        Command(
            name="update",
            help="Update a task (use --done / --no-done to toggle completion)",
            handler=handlers.update,
            arguments=(
                _ID,
                Argument(("-t", "--title")),
                Argument(("-d", "--description")),
                _OPTIONAL_DONE,
            ),
        ),
        Command(
            name="delete",
            help="Delete a task",
            handler=handlers.delete,
            arguments=(_ID,),
        ),
    )
