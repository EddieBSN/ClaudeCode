"""Domain errors. Callers catch these instead of storage-specific exceptions."""


class DomainError(Exception):
    """Base class for all errors raised by the application core."""


class ValidationError(DomainError):
    """A task failed a domain invariant (e.g. blank title)."""


class TaskNotFoundError(DomainError):
    """No task exists with the requested id."""

    def __init__(self, task_id: int) -> None:
        super().__init__(f"No task with id {task_id}")
        self.task_id = task_id
