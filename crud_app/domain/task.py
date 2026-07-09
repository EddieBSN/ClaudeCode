"""The Task entity. Pure data, no framework or storage knowledge."""

from dataclasses import dataclass, replace
from typing import Optional


@dataclass(frozen=True)
class Task:
    """An immutable task. Updates produce a new instance via ``with_changes``."""

    id: Optional[int]
    title: str
    description: str = ""
    done: bool = False

    def with_changes(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        done: Optional[bool] = None,
    ) -> "Task":
        """Return a copy with the given fields replaced; None means keep."""
        return replace(
            self,
            title=self.title if title is None else title,
            description=self.description if description is None else description,
            done=self.done if done is None else done,
        )

    def with_id(self, task_id: int) -> "Task":
        """Return a copy carrying the identity assigned by storage."""
        return replace(self, id=task_id)
