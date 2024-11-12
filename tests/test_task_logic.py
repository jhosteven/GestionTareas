import unittest
from logica import task_logic
from modelo.task_model import Task

class TestTaskLogic(unittest.TestCase):

    def setUp(self):
        task_logic.tasks = []

    def test_create_task(self):
        task = task_logic.create_task(1, "Test Task", "Description", "2023-12-01")
        self.assertEqual(len(task_logic.tasks), 1)
        self.assertIsInstance(task, Task)

    def test_update_task(self):
        task_logic.create_task(1, "Test Task", "Description", "2023-12-01")
        task = task_logic.update_task(1, name="Updated Task")
        self.assertEqual(task.name, "Updated Task")

    def test_delete_task(self):
        task_logic.create_task(1, "Test Task", "Description", "2023-12-01")
        task_logic.delete_task(1)
        self.assertEqual(len(task_logic.tasks), 0)

if __name__ == '__main__':
    unittest.main()
