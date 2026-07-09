"""Contract tests: every TaskRepository adapter must pass the same suite."""

import unittest

from crud_app.adapters.memory_repository import InMemoryTaskRepository
from crud_app.adapters.sqlite_repository import SqliteTaskRepository
from crud_app.domain.errors import TaskNotFoundError
from crud_app.domain.task import Task


class RepositoryContract:
    """Mixin defining the behaviour all adapters must share."""

    def make_repository(self):
        raise NotImplementedError

    def setUp(self):
        self.repository = self.make_repository()

    def test_add_assigns_unique_ids(self):
        first = self.repository.add(Task(id=None, title="one"))
        second = self.repository.add(Task(id=None, title="two"))
        self.assertIsNotNone(first.id)
        self.assertNotEqual(first.id, second.id)

    def test_get_returns_stored_task(self):
        stored = self.repository.add(Task(id=None, title="read me", description="d"))
        self.assertEqual(self.repository.get(stored.id), stored)

    def test_get_unknown_id_raises(self):
        with self.assertRaises(TaskNotFoundError):
            self.repository.get(999)

    def test_list_all_is_ordered_by_id(self):
        titles = ["a", "b", "c"]
        for title in titles:
            self.repository.add(Task(id=None, title=title))
        self.assertEqual([t.title for t in self.repository.list_all()], titles)

    def test_update_replaces_task(self):
        stored = self.repository.add(Task(id=None, title="before"))
        updated = self.repository.update(stored.with_changes(title="after", done=True))
        self.assertEqual(self.repository.get(stored.id), updated)
        self.assertTrue(updated.done)

    def test_update_unknown_id_raises(self):
        with self.assertRaises(TaskNotFoundError):
            self.repository.update(Task(id=999, title="ghost"))

    def test_delete_removes_task(self):
        stored = self.repository.add(Task(id=None, title="doomed"))
        self.repository.delete(stored.id)
        with self.assertRaises(TaskNotFoundError):
            self.repository.get(stored.id)

    def test_delete_unknown_id_raises(self):
        with self.assertRaises(TaskNotFoundError):
            self.repository.delete(999)


class InMemoryRepositoryTest(RepositoryContract, unittest.TestCase):
    def make_repository(self):
        return InMemoryTaskRepository()


class SqliteRepositoryTest(RepositoryContract, unittest.TestCase):
    def make_repository(self):
        return SqliteTaskRepository(":memory:")

    def tearDown(self):
        self.repository.close()


if __name__ == "__main__":
    unittest.main()
