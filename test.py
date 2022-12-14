import unittest

from days import (
    day1, day2, day3, day4,
    day5, day6, day7, day8, day9,
    day10
)


class TestAoC(unittest.TestCase):

    def test_day1(self):
        day1.run('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day1.txt')
        day1.run_opt('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day1.txt')

    def test_day2(self):
        day2.run_pt1('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day2.txt')
        day2.run_pt2('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day2.txt')

    def test_day3(self):
        day3.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day3.txt')
        day3.run_pt1_better('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day3.txt')
        day3.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day3.txt')
        day3.run_pt2_better('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day3.txt')

    def test_day4(self):
        day4.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day4.txt')
        day4.run_pt1_better('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day4.txt')
        day4.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day4.txt')
        day4.run_pt2_better('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day4.txt')

    def test_day5(self):
        day5.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day5.txt')
        day5.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day5.txt')

    def test_day6(self):
        day6.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day6.txt')
        day6.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day6.txt')

    def test_day7(self):
        day7.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day7.txt')
        day7.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day7.txt')

    def test_day8(self):
        day8.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day8.txt')
        day8.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day8.txt')

    def test_day9(self):
        day9.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day9.txt')
        day9.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day9.txt')

    def test_day9(self):
        day10.run_pt1_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day10.txt')
        day10.run_pt2_first_pass('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day10.txt')


if __name__ == '__main__':
    unittest.main()