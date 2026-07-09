"""In-memory adapter. Used in tests and as a reference implementation."""

from itertools import count
from typing import Dict, List

from ..domain.errors import TaskNotFoundError
from ..domain.task import Task
from ..ports.repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    """Stores tasks in a dict keyed by id."""

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id = count(start=1)

    def add(self, task: Task) -> Task:
        stored = task.with_id(next(self._next_id))
        self._tasks[stored.id] = stored
        return stored

    def get(self, task_id: int) -> Task:
        self._require_exists(task_id)
        return self._tasks[task_id]

    def list_all(self) -> List[Task]:
        return [self._tasks[task_id] for task_id in sorted(self._tasks)]

    def update(self, task: Task) -> Task:
        self._require_exists(task.id)
        self._tasks[task.id] = task
        return task

    def delete(self, task_id: int) -> None:
        self._require_exists(task_id)
        del self._tasks[task_id]

    def _require_exists(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
