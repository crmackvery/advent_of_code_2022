from typing import Tuple
from collections import deque
import numpy as np


class Monkey:
    def __init__(self, by_three):
        self.items = []
        self.operation = ""
        self.operation_value = ""
        self.test_value = 0
        self.true_recipient = 0
        self.false_recipient = 0
        self.inspect_count = 0
        self.by_three = by_three

    def inspect_and_throw_next_item(self, modulo) -> Tuple[int, int]:
        self.inspect_count += 1
        value = self.items.pop(0)
        if modulo > 0:
            value = value % modulo
        opt_val = value
        if "old" not in self.operation_value:
            opt_val = int(self.operation_value)

        new_worry = 0
        if self.operation == "+":
            new_worry = value + opt_val
        elif self.operation == "*":
            new_worry = value * opt_val

        if self.by_three:
            new_worry = int(np.floor(new_worry / 3))

        if new_worry % self.test_value:
            return self.false_recipient, new_worry
        else:
            return self.true_recipient, new_worry


def build_monkey(monkey_text, by_three) -> Monkey:
    monkey = Monkey(by_three)
    parts = monkey_text.split("\n")
    monkey.items = [int(x) for x in parts[1].split(":")[1].split(",")]
    monkey.operation = parts[2].split(" = ")[1].split(" ")[1]
    monkey.operation_value = parts[2].split(" = ")[1].split(" ")[2]
    monkey.test_value = int(parts[3].split("by ")[1])
    monkey.true_recipient = int(parts[4].split(" ")[-1])
    monkey.false_recipient = int(parts[5].split(" ")[-1])

    return monkey


def build_monkeys(file_input, by_three) -> list:
    monkeys = []
    for monkey in file_input.split("\n\n"):
        monkeys.append(build_monkey(monkey, by_three))

    return monkeys


def run_rounds(monkeys, n_rounds, modulo: int = 0) -> list:
    for i in range(n_rounds):
        for monkey in monkeys:
            while monkey.items:
                recipient, new_item = monkey.inspect_and_throw_next_item(modulo)
                monkeys[recipient].items.append(new_item)

    return monkeys


def monkey_business(monkeys) -> int:
    inspection_counts = []
    for monkey in monkeys:
        inspection_counts.append(monkey.inspect_count)

    return np.prod(sorted(inspection_counts, reverse=True)[0:2])


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    monkeys = build_monkeys(f.read(), True)
    monkeys = run_rounds(monkeys, 20)
    print("Day 11 - Part 1: " + str(monkey_business(monkeys)))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    monkeys = build_monkeys(f.read(), False)
    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.test_value # 96577
    monkeys = run_rounds(monkeys, 10000, modulo)
    print("Day 11 - Part 2: " + str(monkey_business(monkeys)))
    f.close()
