"""Composition root: the only module that knows about concrete adapters.

Argparse subparsers dispatch straight to handler methods via ``set_defaults``,
so there is no if/elif command chain anywhere.
"""

import argparse
import sys

from ..adapters.sqlite_repository import SqliteTaskRepository
from ..domain.errors import DomainError
from ..domain.validation import TaskValidator
from ..services.task_service import TaskService
from .commands import TaskCommands
from .presenter import TaskPresenter

_DEFAULT_DATABASE = "tasks.db"


def build_parser(commands: TaskCommands) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tasks", description="Task CRUD manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create = subparsers.add_parser("create", help="Create a task")
    create.add_argument("title")
    create.add_argument("-d", "--description", default="")
    create.set_defaults(handler=commands.create)

    show = subparsers.add_parser("show", help="Show one task")
    show.add_argument("id", type=int)
    show.set_defaults(handler=commands.show)

    list_ = subparsers.add_parser("list", help="List all tasks")
    list_.set_defaults(handler=commands.list)

    update = subparsers.add_parser("update", help="Update a task")
    update.add_argument("id", type=int)
    update.add_argument("-t", "--title")
    update.add_argument("-d", "--description")
    done_group = update.add_mutually_exclusive_group()
    done_group.add_argument("--done", dest="done", action="store_true", default=None)
    done_group.add_argument("--not-done", dest="done", action="store_false")
    update.set_defaults(handler=commands.update)

    delete = subparsers.add_parser("delete", help="Delete a task")
    delete.add_argument("id", type=int)
    delete.set_defaults(handler=commands.delete)

    return parser


def main(argv=None) -> int:
    repository = SqliteTaskRepository(_DEFAULT_DATABASE)
    service = TaskService(repository, TaskValidator())
    commands = TaskCommands(service, TaskPresenter())

    args = build_parser(commands).parse_args(argv)
    try:
        print(args.handler(args))
    except DomainError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    finally:
        repository.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
