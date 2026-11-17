import unittest
from app import add, multiply, subtract

class TestApplication(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 25)

    def test_subtract(self):
        self.assertEqual(subtract(50, 20), 30)

if __name__ == "__main__":
    unittest.main()
