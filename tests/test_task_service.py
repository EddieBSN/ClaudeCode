"""Service tests run against the in-memory adapter via the port."""

import unittest

from crud_app.adapters.memory_repository import InMemoryTaskRepository
from crud_app.domain.errors import TaskNotFoundError, ValidationError
from crud_app.domain.validation import TaskValidator
from crud_app.services.task_service import TaskService


class TaskServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = TaskService(InMemoryTaskRepository(), TaskValidator())

    def test_create_returns_task_with_id(self):
        task = self.service.create("Write tests", "cover the service")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Write tests")
        self.assertFalse(task.done)

    def test_create_rejects_blank_title(self):
        with self.assertRaises(ValidationError):
            self.service.create("   ")

    def test_create_rejects_overlong_title(self):
        with self.assertRaises(ValidationError):
            self.service.create("x" * 201)

    def test_get_returns_created_task(self):
        created = self.service.create("Find me")
        self.assertEqual(self.service.get(created.id), created)

    def test_list_all_returns_tasks_in_creation_order(self):
        self.service.create("first")
        self.service.create("second")
        self.assertEqual([t.title for t in self.service.list_all()], ["first", "second"])

    def test_update_changes_only_given_fields(self):
        created = self.service.create("original", "keep me")
        updated = self.service.update(created.id, done=True)
        self.assertEqual(updated.title, "original")
        self.assertEqual(updated.description, "keep me")
        self.assertTrue(updated.done)

    def test_update_validates_new_title(self):
        created = self.service.create("valid")
        with self.assertRaises(ValidationError):
            self.service.update(created.id, title="  ")

    def test_update_unknown_id_raises(self):
        with self.assertRaises(TaskNotFoundError):
            self.service.update(42, title="nope")

    def test_delete_removes_task(self):
        created = self.service.create("temporary")
        self.service.delete(created.id)
        with self.assertRaises(TaskNotFoundError):
            self.service.get(created.id)


if __name__ == "__main__":
    unittest.main()
