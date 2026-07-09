"""Composition root: the only module that knows about concrete adapters."""

import sys
from typing import List, Optional

from crud_app.adapters.sqlite_repository import SqliteTaskRepository
from crud_app.cli.commands import TaskCommands
from crud_app.cli.parser import build_parser
from crud_app.cli.presenter import TaskPresenter
from crud_app.cli.registry import command_table
from crud_app.domain.errors import DomainError
from crud_app.domain.factory import TaskFactory
from crud_app.domain.validation import TaskValidator
from crud_app.services.task_service import TaskService

_DEFAULT_DATABASE = "tasks.db"


def main(argv: Optional[List[str]] = None) -> int:
    repository = SqliteTaskRepository(_DEFAULT_DATABASE)
    try:
        return _run(_compose(repository), argv)
    finally:
        repository.close()


def _compose(repository: SqliteTaskRepository) -> TaskCommands:
    service = TaskService(repository, TaskValidator())
    return TaskCommands(service, TaskPresenter(), TaskFactory())


def _run(handlers: TaskCommands, argv: Optional[List[str]]) -> int:
    args = build_parser(command_table(handlers)).parse_args(argv)
    try:
        print(args.handler(args))
    except DomainError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
