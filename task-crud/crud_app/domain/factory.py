"""Constructs new, unsaved Task instances."""

from crud_app.domain.task import Task


class TaskFactory:
    """The single place that knows how a brand-new Task is assembled."""

    def new_task(self, title: str, description: str = "") -> Task:
        return Task(id=None, title=title, description=description, done=False)
