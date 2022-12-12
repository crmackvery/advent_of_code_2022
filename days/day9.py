import numpy as np
import math

DIRECTIONS = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}


def build_grid():
    return np.zeros(shape=(1000, 1000), dtype=int)


def are_adjacent(a, b) -> bool:
    if math.fabs(a[0] - b[0]) > 1.0 or math.fabs(a[1] - b[1]) > 1.0:
        return False

    return True


def move_head(head, direction) -> list:
    head += DIRECTIONS[direction]

    return head


def move_tail(head, tail) -> list:
    # Doesn't move if result of move is a diagonal adjacent...
    if not are_adjacent(head, tail):
        dx = head[0] - tail[0]
        dy = head[1] - tail[1]
        if not dx:
            d = 1 if dy > 0 else -1
            tail[1] += d
        elif not dy:
            d = 1 if dx > 0 else -1
            tail[0] += d
        else:
            d_x = 1 if dx > 0 else -1
            d_y = 1 if dy > 0 else -1
            tail[0] += d_x
            tail[1] += d_y

    return tail


def run_commands(file_contents) -> int:
    grid = build_grid()

    h = np.array([100, 100])
    t = np.array([100, 100])

    for line in file_contents.split("\n"):
        direction, amount_s = line.split(" ")
        amount = int(amount_s)
        for i in range(0, amount):
            h = move_head(h, direction)
            t = move_tail(h, t)
            grid[t[1], t[0]] = 1

    return np.sum(grid)


def run_commands_pt2(file_contents) -> int:
    grid = build_grid()

    h = np.array([100, 100])
    t = np.ones(shape=(9, 2), dtype=int) * 100

    for line in file_contents.split("\n"):
        direction, amount_s = line.split(" ")
        amount = int(amount_s)
        for i in range(0, amount):
            h = move_head(h, direction)
            t[0] = move_tail(h, t[0])
            for j in range(1, len(t)):
                t[j] = move_tail(t[j-1], t[j])

            grid[t[8][1], t[8][0]] = 1

    return np.sum(grid)


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 9 - Part 1: " + str(run_commands(f.read())))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 9 - Part 2: " + str(run_commands_pt2(f.read())))
    f.close()
