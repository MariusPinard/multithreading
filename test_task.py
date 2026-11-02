import unittest

import numpy as np

from task import Task


class TestTask(unittest.TestCase):
    def test_solve(self):
        task = Task()
        task.work()
        np.testing.assert_allclose(task.a @ task.x, task.b)


if __name__ == "__main__":
    unittest.main()
