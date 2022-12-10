class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


class Directory:
    def __init__(self):
        self.name = ""
        self.files = []
        self.subdirectories = []
        self.parent = None
        self.file_size = 0

    def add_file(self, file_name, file_size):
        self.files.append(File(file_name, file_size))
        self.file_size += int(file_size)

    def add_subdirectory_by_name(self, subdirectory_name):
        found = False
        for sub in self.subdirectories:
            if sub.name == subdirectory_name:
                found = True
                break

        if not found:
            subdir = Directory()
            subdir.name = subdirectory_name
            subdir.parent = self
            self.subdirectories.append(subdir)

    def total_size(self, size):
        for s in self.subdirectories:
            size = s.total_size(size)

        return self.file_size + size

    def find_sub_dir(self, to_find):
        for sub in self.subdirectories:
            if sub.name == to_find:
                return sub


def execute_command(state, command):
    if command.startswith("cd"):
        if command == "cd ..":
            state["CWD"] = state["CWD"].parent
        elif command == "cd /":
            state["CWD"] = state["top"]
        else:
            state["CWD"] = state["CWD"].find_sub_dir(command.split(" ")[1])
    elif command.startswith("ls"):
        for line in command.split("\n"):
            if line.startswith("dir"):
                state["CWD"].add_subdirectory_by_name(line.split(" ")[1])
            elif not line.startswith("ls"):
                state["CWD"].add_file(line.split(" ")[1], line.split(" ")[0])
    return state


def calculate_pt_1(directory, valid_sum):
    for s in directory.subdirectories:
        valid_sum = calculate_pt_1(s, valid_sum)

    size = directory.total_size(0)
    if size <= 100000:
        return size + valid_sum
    else:
        return valid_sum


def find_dir_to_delete(directory, space_needed, smallest_acceptable):
    for s in directory.subdirectories:
        smallest_acceptable = find_dir_to_delete(s, space_needed, smallest_acceptable)

    d_size = directory.total_size(0)
    if space_needed < d_size < smallest_acceptable:
        smallest_acceptable = d_size

    return smallest_acceptable


def calculate_pt_2(top_dir):
    total_space = top_dir.total_size(0)
    unused_space = 70000000 - total_space
    space_needed = 30000000 - unused_space
    return find_dir_to_delete(top_dir, space_needed, total_space)


def parse_and_run(file_contents):
    top_dir = Directory()
    top_dir.name = "/"
    state = {"CWD": top_dir, "top": top_dir}
    for idx, x in enumerate(file_contents.split("$")):
        state = execute_command(state, x.strip())
    return calculate_pt_1(state["top"], 0)


def parse_and_run_pt2(file_contents):
    top_dir = Directory()
    top_dir.name = "/"
    state = {"CWD": top_dir, "top": top_dir}
    for idx, x in enumerate(file_contents.split("$")):
        state = execute_command(state, x.strip())
    return calculate_pt_2(state["top"])


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 7 - Part 1: " + str(parse_and_run(f.read())))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 7 - Part 2: " + str(parse_and_run_pt2(f.read())))
    f.close()
