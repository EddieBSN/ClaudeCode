"""SQLite adapter. Swappable with any other TaskRepository implementation."""

import sqlite3
from typing import List

from ..domain.errors import TaskNotFoundError
from ..domain.task import Task
from ..ports.repository import TaskRepository

_SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    description TEXT    NOT NULL,
    done        INTEGER NOT NULL
)
"""


class SqliteTaskRepository(TaskRepository):
    """Persists tasks to a SQLite database file (or ':memory:')."""

    def __init__(self, database_path: str) -> None:
        self._connection = sqlite3.connect(database_path)
        self._connection.row_factory = sqlite3.Row
        with self._connection:
            self._connection.execute(_SCHEMA)

    def add(self, task: Task) -> Task:
        with self._connection:
            cursor = self._connection.execute(
                "INSERT INTO tasks (title, description, done) VALUES (?, ?, ?)",
                (task.title, task.description, int(task.done)),
            )
        return task.with_id(cursor.lastrowid)

    def get(self, task_id: int) -> Task:
        row = self._connection.execute(
            "SELECT * FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
        if row is None:
            raise TaskNotFoundError(task_id)
        return self._to_task(row)

    def list_all(self) -> List[Task]:
        rows = self._connection.execute("SELECT * FROM tasks ORDER BY id").fetchall()
        return [self._to_task(row) for row in rows]

    def update(self, task: Task) -> Task:
        with self._connection:
            cursor = self._connection.execute(
                "UPDATE tasks SET title = ?, description = ?, done = ? WHERE id = ?",
                (task.title, task.description, int(task.done), task.id),
            )
        if cursor.rowcount == 0:
            raise TaskNotFoundError(task.id)
        return task

    def delete(self, task_id: int) -> None:
        with self._connection:
            cursor = self._connection.execute(
                "DELETE FROM tasks WHERE id = ?", (task_id,)
            )
        if cursor.rowcount == 0:
            raise TaskNotFoundError(task_id)

    def close(self) -> None:
        self._connection.close()

    @staticmethod
    def _to_task(row: sqlite3.Row) -> Task:
        return Task(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            done=bool(row["done"]),
        )
