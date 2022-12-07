import queue


def parse_stack(stack_lines):
    crates = {}
    for x in range(1, 10):
        crates[x] = queue.LifoQueue()

    for line in reversed(stack_lines):
        if "[" in line:
            for i, crate in enumerate(line[1::4]):
                if crate != " ":
                    crates[i+1].put(crate)

    return crates


def parse_file(file_contents):
    stack, instruction_text = file_contents.split("\n\n")
    crates = parse_stack(stack.split("\n"))

    instructions = []
    for line in instruction_text.split("\n"):
        parts = line.split(" ")
        instructions.append([int(parts[1]), int(parts[3]), int(parts[5])])

    return crates, instructions


def run_operations(crates, instructions):
    for instruction in instructions:
        for i in range(1, instruction[0]+1):
            crates[instruction[2]].put(crates[instruction[1]].get())

    return crates


def run_operations_pt2(crates, instructions):
    for instruction in instructions:
        load = queue.LifoQueue()
        for i in range(1, instruction[0]+1):
            load.put(crates[instruction[1]].get())
        while not load.empty():
            crates[instruction[2]].put(load.get())

    return crates


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    crates, instructions = parse_file(f.read())
    crates = run_operations(crates, instructions)
    output = ""
    for i, crate in crates.items():
        if not crate.empty():
            output += str(crate.get())
    print("Day 5 - Part 1: " + output)
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    crates, instructions = parse_file(f.read())
    crates = run_operations_pt2(crates, instructions)
    output = ""
    for i, crate in crates.items():
        if not crate.empty():
            output += str(crate.get())
    print("Day 5 - Part 2: " + output)
    f.close()
