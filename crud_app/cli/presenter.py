"""Turns domain objects into console text. The only place that formats output."""

from typing import List

from ..domain.task import Task


class TaskPresenter:
    """Renders tasks for the terminal."""

    def render_task(self, task: Task) -> str:
        marker = "x" if task.done else " "
        line = f"[{marker}] #{task.id} {task.title}"
        if task.description:
            line += f" — {task.description}"
        return line

    def render_list(self, tasks: List[Task]) -> str:
        if not tasks:
            return "No tasks yet."
        return "\n".join(self.render_task(task) for task in tasks)
