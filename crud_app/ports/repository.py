"""The storage port. Services depend on this contract, never on an adapter.

Any implementation must honour the same behaviour (Liskov substitution):

- ``add`` assigns and returns the task with a new unique id.
- ``get`` and ``update`` raise TaskNotFoundError for unknown ids.
- ``delete`` raises TaskNotFoundError for unknown ids.
- ``list_all`` returns tasks ordered by id.
"""

from abc import ABC, abstractmethod
from typing import List

from ..domain.task import Task


class TaskRepository(ABC):
    """Abstract CRUD storage for tasks."""

    @abstractmethod
    def add(self, task: Task) -> Task:
        """Persist a new task and return it with its assigned id."""

    @abstractmethod
    def get(self, task_id: int) -> Task:
        """Return the task with the given id."""

    @abstractmethod
    def list_all(self) -> List[Task]:
        """Return every stored task, ordered by id."""

    @abstractmethod
    def update(self, task: Task) -> Task:
        """Replace the stored task having ``task.id`` and return it."""

    @abstractmethod
    def delete(self, task_id: int) -> None:
        """Remove the task with the given id."""
