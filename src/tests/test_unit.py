import unittest
from src.business_logic import add, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 4), -4)


if __name__ == "__main__":
    unittest.main()
