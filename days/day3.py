import string

letters = list(string.ascii_lowercase)
letters.extend(list(string.ascii_uppercase))


def solve_line(line):
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    duplicate = ""
    for a_char in a:
        if a_char in b:
            duplicate = a_char

    return letters.index(duplicate) + 1


def solve_line_better(line):
    return letters.index(''.join(set(line[:len(line) // 2]).intersection(line[len(line) // 2:]))) + 1


def solve_group(three_elves):
    return letters.index(''.join(set(three_elves[0]).intersection(three_elves[1]).intersection(three_elves[2]))) + 1


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 3 - Part 1: " + str(sum(solve_line(x) for x in f.read().split("\n"))))
    f.close()


def run_pt1_better(file_name):
    f = open(file_name, "r")
    print("Day 3 - Part 1 - Better: " + str(sum(solve_line_better(x) for x in f.read().split("\n"))))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    all_data = f.read().split("\n")
    total = 0
    for idx, x in enumerate(all_data[::3]):
        total += solve_group(all_data[(idx*3):(idx*3)+3])
    print("Day 3 - Part 2: " + str(total))
    f.close()


def run_pt2_better(file_name):
    f = open(file_name, "r")
    all_data = f.read().split("\n")
    print("Day 3 - Part 2 - Better: " + str(sum(solve_group(all_data[(idx*3):(idx*3)+3]) for idx, x in
                                                enumerate(all_data[::3]))))
    f.close()
