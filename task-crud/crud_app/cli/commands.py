"""CLI command handlers. Thin: parse args in, delegate to the service, present."""

import argparse

from crud_app.cli.presenter import TaskPresenter
from crud_app.domain.factory import TaskFactory
from crud_app.services.task_service import TaskService


class TaskCommands:
    """One handler method per subcommand; each returns the text to print."""

    def __init__(
        self,
        service: TaskService,
        presenter: TaskPresenter,
        factory: TaskFactory,
    ) -> None:
        self._service = service
        self._presenter = presenter
        self._factory = factory

    def create(self, args: argparse.Namespace) -> str:
        task = self._service.create(
            self._factory.new_task(args.title, args.description)
        )
        return f"Created: {self._presenter.render_task(task)}"

    def show(self, args: argparse.Namespace) -> str:
        return self._presenter.render_task(self._service.get(args.id))

    def list(self, args: argparse.Namespace) -> str:
        return self._presenter.render_list(self._service.list_all())

    def update(self, args: argparse.Namespace) -> str:
        task = self._service.update(
            args.id, title=args.title, description=args.description, done=args.done
        )
        return f"Updated: {self._presenter.render_task(task)}"

    def delete(self, args: argparse.Namespace) -> str:
        self._service.delete(args.id)
        return f"Deleted task #{args.id}"
