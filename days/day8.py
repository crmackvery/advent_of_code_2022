import math

def make_map(file_contents):
    tree_map = []
    for row, line in enumerate(file_contents.split("\n")):
        tree_row = []
        for val in list(line):
            tree_row.append(int(val))
        tree_map.append(tree_row)

    return tree_map


def is_treeline_visible(treeline, tree_height):
    for tree in treeline:
        if tree >= tree_height:
            return False

    return True


def is_tree_visible(row_idx, col_idx, tree_map):
    if row_idx == 0 or col_idx == 0 or row_idx == len(tree_map) - 1 or col_idx == len(tree_map[0]) - 1:
        return True

    tree_height = tree_map[row_idx][col_idx]
    if tree_height == 0:
        return False

    # Top
    treeline = []
    for i in range(0, row_idx):
        treeline.append(tree_map[i][col_idx])
    if is_treeline_visible(treeline, tree_height):
        return True

    # Bottom
    treeline = []
    for i in range(row_idx+1, len(tree_map)):
        treeline.append(tree_map[i][col_idx])
    if is_treeline_visible(treeline, tree_height):
        return True

    # Left
    treeline = []
    for i in range(0, col_idx):
        treeline.append(tree_map[row_idx][i])
    if is_treeline_visible(treeline, tree_height):
        return True

    # Right
    treeline = []
    for i in range(col_idx+1, len(tree_map[0])):
        treeline.append(tree_map[row_idx][i])
    if is_treeline_visible(treeline, tree_height):
        return True

    return False


def scenic_score(row_idx, col_idx, tree_map):
    tree_height = tree_map[row_idx][col_idx]

    scores = []
    # Top
    score = 0
    for i in reversed(range(0, row_idx)):
        if tree_map[i][col_idx] < tree_height:
            score += 1
        else:
            score += 1
            break

    scores.append(score)

    # Bottom
    score = 0
    for i in range(row_idx+1, len(tree_map)):
        if tree_map[i][col_idx] < tree_height:
            score += 1
        else:
            score += 1
            break

    scores.append(score)

    # Left
    score = 0
    for i in reversed(range(0, col_idx)):
        if tree_map[row_idx][i] < tree_height:
            score += 1
        else:
            score += 1
            break

    scores.append(score)

    # Right
    score = 0
    for i in range(col_idx+1, len(tree_map[0])):
        if tree_map[row_idx][i] < tree_height:
            score += 1
        else:
            score += 1
            break

    scores.append(score)

    return math.prod(scores)


def find_visible(tree_map):
    visible_trees = []

    for row_idx, row in enumerate(tree_map):
        for col_idx, col in enumerate(list(row)):
            if is_tree_visible(row_idx, col_idx, tree_map):
                visible_trees.append(str(row_idx) + str(col_idx))

    return visible_trees


def find_highest_scenic_score(tree_map):
    high_score = 0
    for row_idx, row in enumerate(tree_map):
        for col_idx, col in enumerate(list(row)):
            score = scenic_score(row_idx, col_idx, tree_map)
            if score > high_score:
                high_score = score

    return high_score


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    tree_map = make_map(f.read())
    print("Day 8 - Part 1: " + str(len(find_visible(tree_map))))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    tree_map = make_map(f.read())
    print("Day 8 - Part 2: " + str(find_highest_scenic_score(tree_map)))
    f.close()


# Numpy makes this 98% simpler...
# import numpy as np
# grid = np.array([list(x.strip()) for x in open(file_name)], int)
# part1 = np.zeros_like(grid)
# part2 = np.ones_like(grid)
#
# for _ in range(4):
#     for x, y in np.ndindex(grid.shape):
#         lower = [t < grid[x, y] for t in grid[x, y + 1:]]
#
#         part1[x, y] |= all(lower)
#         part2[x, y] *= next((i + 1 for i, t in enumerate(lower) if ~t), len(lower))
#
#     grid, part1, part2 = map(np.rot90, [grid, part1, part2])
#
# print(part1.sum(), part2.max())
