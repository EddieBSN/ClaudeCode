"""Use cases. Depends only on the repository port and the validator."""

from typing import List, Optional

from ..domain.task import Task
from ..domain.validation import TaskValidator
from ..ports.repository import TaskRepository


class TaskService:
    """Application-facing CRUD operations for tasks."""

    def __init__(self, repository: TaskRepository, validator: TaskValidator) -> None:
        self._repository = repository
        self._validator = validator

    def create(self, title: str, description: str = "") -> Task:
        task = Task(id=None, title=title, description=description)
        self._validator.validate(task)
        return self._repository.add(task)

    def get(self, task_id: int) -> Task:
        return self._repository.get(task_id)

    def list_all(self) -> List[Task]:
        return self._repository.list_all()

    def update(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        done: Optional[bool] = None,
    ) -> Task:
        updated = self._repository.get(task_id).with_changes(
            title=title, description=description, done=done
        )
        self._validator.validate(updated)
        return self._repository.update(updated)

    def delete(self, task_id: int) -> None:
        self._repository.delete(task_id)
