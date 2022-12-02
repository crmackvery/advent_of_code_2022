import unittest

from days import day1, day2


class TestAoC(unittest.TestCase):

    def test_day1(self):
        day1.run('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day1.txt')
        day1.run_opt('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day1.txt')

    def test_day2(self):
        day2.run_pt1('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day2.txt')
        day2.run_pt2('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day2.txt')
