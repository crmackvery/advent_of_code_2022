from typing import Tuple
import string
import numpy as np

letters = list(string.ascii_lowercase)


def make_grid(file_lines):
    start = (0, 0)
    end = (0, 0)
    starts = []
    grid = np.zeros((len(file_lines), len(file_lines[0])), dtype=int)
    for y_idx, line in enumerate(file_lines):
        for x_idx, c in enumerate(line):
            if c == "S":
                start = (y_idx, x_idx)
                starts.append((y_idx, x_idx))
                grid[y_idx, x_idx] = 1
            elif c == "E":
                end = (y_idx, x_idx)
                grid[y_idx, x_idx] = len(letters)
            else:
                if c == "a":
                    starts.append((y_idx, x_idx))
                grid[y_idx, x_idx] = letters.index(c) + 1

    return grid, start, end, starts


def get_neighbors(matrix, node) -> list:
    x_min = 0
    y_min = 0
    x_max = len(matrix) - 1
    y_max = len(matrix[0]) - 1
    x, y = node

    node_height = matrix[x][y] - 2

    neighbors = []

    # Check edges and relative heights
    if (x_min < x) and (node_height < matrix[x - 1][y]):
        neighbors.append((x - 1, y))
    if (x < x_max) and (node_height < matrix[x + 1][y]):
        neighbors.append((x + 1, y))
    if (y_min < y) and (node_height < matrix[x][y - 1]):
        neighbors.append((x, y - 1))
    if (y < y_max) and (node_height < matrix[x][y + 1]):
        neighbors.append((x, y + 1))

    return neighbors


def bfs(grid, end) -> dict:
    steps = [end]
    levels = dict()
    levels[end] = 0

    while steps:
        current = steps.pop(0)
        for neighbor in get_neighbors(grid, current):
            if neighbor not in levels:
                levels[neighbor] = levels[current] + 1
                steps.append(neighbor)

    return levels


def find_shortest_path(grid, start, end, starts) -> Tuple[int, int]:
    levels = bfs(grid, end)
    totals = [levels.get(point) for point in starts if levels.get(point)]
    return levels[start], min(totals)


def run_first_pass(file_name):
    f = open(file_name, "r")
    grid, start, end, starts = make_grid(f.read().split("\n"))
    pt1, pt2 = find_shortest_path(grid, start, end, starts)
    print("Day 12 - Part 1: " + str(pt1))
    print("Day 12 - Part 1: " + str(pt2))
    f.close()


