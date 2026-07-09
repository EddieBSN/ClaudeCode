"""Validation of domain invariants, separated from the entity and the service."""

from crud_app.domain.errors import ValidationError
from crud_app.domain.task import Task

_MAX_TITLE_LENGTH = 200


class TaskValidator:
    """Checks Task invariants. Raises ValidationError on the first violation."""

    def validate(self, task: Task) -> None:
        self._require_title(task.title)
        self._limit_title_length(task.title)

    def _require_title(self, title: str) -> None:
        if not title.strip():
            raise ValidationError("Title must not be blank")

    def _limit_title_length(self, title: str) -> None:
        if len(title) > _MAX_TITLE_LENGTH:
            raise ValidationError(
                f"Title must be at most {_MAX_TITLE_LENGTH} characters"
            )
