import unittest
from modelo.task_model import Task

class TestTaskModel(unittest.TestCase):

    def test_task_creation(self):
        task = Task(1, "Test Task", "Description", "2023-12-01")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.description, "Description")
        self.assertEqual(task.due_date, "2023-12-01")
        self.assertEqual(task.status, "Pendiente")

if __name__ == '__main__':
    unittest.main()
