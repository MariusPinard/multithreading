import unittest
import numpy as np
from task import Task


class TestTask(unittest.TestCase):
    def test_solve(self):
        task = Task()
        task.solve()
        np.testing.assert_allclose(task.A @ task.x, task.B)


if __name__ == "__main__":
    unittest.main()
