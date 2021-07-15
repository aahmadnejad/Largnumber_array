from unittest import TestCase
import unittest

from main import large_number


class Challenge2TestCase(TestCase):

    def setUp(self) -> None:
        self.test_cases = [
            ([44, 50, 6, 5, 9], 9655044),
            ([55, 99, 3648, 2, 7], 9975536482),
            ([88, 66, 789, 324, 8524, 8523], 888524852378966324),
            ([67, 36, 7, 0], 767360),
            ([987, 98, 7, 0, 87634, 93, 4, 7], 9898793876347740),
            ([2, 2, 2, 22, 222, 33, 202, 21], 332222222221202),
            ([3, 0, 8, 6, 7, 6, 0], 8766300),
            ([69699, 333, 68688], 6969968688333),
            ([300, 311, 322, 355, 344, 30], 35534432231130300)

        ]

    def test_numbers(self):
        for ts in self.test_cases:
            self.assertEqual(large_number(ts[0]), ts[1])


if __name__ == "__main__":
    unittest.main()
