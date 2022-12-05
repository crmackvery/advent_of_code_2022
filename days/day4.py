def contained(min_v, max_v, x):
    ret = False
    if int(min_v) <= int(x) <= int(max_v):
        ret = True

    return ret


def does_fully_contain(line):
    ret = 0
    parts = line.split(",")
    a = parts[0].split("-")
    b = parts[1].split("-")
    if contained(a[0], a[1], b[0]) and contained(a[0], a[1], b[1]):
        ret = 1
    elif contained(b[0], b[1], a[0]) and contained(b[0], b[1], a[1]):
        ret = 1

    return ret


def does_fully_contain_better(line):
    ret = 0
    parts = line.split(",")
    a = parts[0].split("-")
    b = parts[1].split("-")
    a_min = int(a[0])
    a_max = int(a[1])
    b_min = int(b[0])
    b_max = int(b[1])
    a_range = range(a_min, a_max + 1)
    b_range = range(b_min, b_max + 1)
    if b_min in a_range and b_max in a_range:
        ret = 1
    elif a_min in b_range and a_max in b_range:
        ret = 1

    return ret


def does_overlap(line):
    ret = 0
    parts = line.split(",")
    a = parts[0].split("-")
    b = parts[1].split("-")
    if contained(a[0], a[1], b[0]) and contained(a[0], a[1], b[1]):
        ret = 1
    elif contained(b[0], b[1], a[0]) and contained(b[0], b[1], a[1]):
        ret = 1
    elif contained(a[0], a[1], b[0]) or contained(a[0], a[1], b[1]):
        ret = 1
    elif contained(b[0], b[1], a[0]) or contained(b[0], b[1], a[1]):
        ret = 1

    return ret


def does_overlap_better(line):
    ret = 0
    parts = line.split(",")
    a = parts[0].split("-")
    b = parts[1].split("-")
    a_min = int(a[0])
    a_max = int(a[1])
    b_min = int(b[0])
    b_max = int(b[1])
    if len(range(max(a_min, b_min), min(a_max, b_max) + 1)) > 0:
        ret = 1

    return ret


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 4 - Part 1: " + str(sum(does_fully_contain(x) for x in f.read().split("\n"))))
    f.close()


def run_pt1_better(file_name):
    f = open(file_name, "r")
    print("Day 4 - Part 1 - Better: " + str(sum(does_fully_contain_better(x) for x in f.read().split("\n"))))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 4 - Part 1: " + str(sum(does_overlap(x) for x in f.read().split("\n"))))
    f.close()


def run_pt2_better(file_name):
    f = open(file_name, "r")
    print("Day 4 - Part 1 - Better: " + str(sum(does_overlap_better(x) for x in f.read().split("\n"))))
    f.close()
