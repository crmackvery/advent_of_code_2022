from typing import Tuple
from collections import deque
import numpy as np

SOI = [20, 60, 100, 140, 180, 220]


def draw_a_grid(grid):
    disp_string = ""
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == 0:
                disp_string += "."
            else:
                disp_string += "#"

        disp_string += "\n"

    print(disp_string)


def build_empty_grid():
    return np.zeros(shape=(6, 40), dtype=int)


def find_index_of_nth_cycle(commands, n) -> int:
    cycle = 0
    idx = 0
    for c in commands:
        if c == "noop":
            cycle += 1
        else:
            cycle += 2

        idx += 1
        if cycle >= n:
            break

    if cycle >= n:
        idx -= 1

    return idx


def get_signals_of_interest(commands, values) -> int:
    signals = []
    for s in SOI:
        t = sum(values[:find_index_of_nth_cycle(commands, s)])
        signals.append((sum(values[:find_index_of_nth_cycle(commands, s)]) + 1) * s)

    return sum(signals)


def parse_commands(file_contents) -> Tuple[list, list]:
    commands = []
    values = []
    for line in file_contents.split("\n"):
        if "noop" in line:
            commands.append(line)
            values.append(0)
        else:
            commands.append(line.split(" ")[0])
            values.append(int(line.split(" ")[1]))

    return commands, values


def draw_sprite_position(register) -> np.array:
    sprite = build_empty_grid()
    for i in range(register - 1, register + 2):
        if -1 < i < 40:
            for y in range(6):
                sprite[y, i] = 1
    return sprite


def draw_stuff(commands, values) -> str:
    coms = deque(commands)
    vals = deque(values)
    crt = build_empty_grid()
    register = 1
    cycle = 0
    is_done = False
    state = {"com": "", "pending": False, "val": 0, "wait": 0}

    while not is_done:
        if not state["pending"]:
            state["com"] = coms.popleft()
            state["val"] = vals.popleft()
            state["wait"] = 0
            if "addx" in state["com"]:
                state["pending"] = True
            elif len(coms) == 0:
                is_done = True
        else:
            state["wait"] = 1

        sprite = draw_sprite_position(register)
        tmp = build_empty_grid()
        tmp[int(np.floor(cycle / 40)), cycle % 40] = 1
        crt = np.add(crt, np.multiply(sprite, tmp))
        cycle += 1

        if state["wait"] == 1:
            register += state["val"]
            state["pending"] = False
            if len(coms) == 0:
                is_done = True

    return crt


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    commands, vals = parse_commands(f.read())
    print("Day 10 - Part 1: " + str(get_signals_of_interest(commands, vals)))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    commands, vals = parse_commands(f.read())
    crt = draw_stuff(commands, vals)
    print("Day 10 - Part 2: ")
    print(draw_a_grid(crt))

    f.close()
