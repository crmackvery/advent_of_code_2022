def update_top_three(top_three, new_value):
    if new_value > top_three[0]:
        top_three.insert(0, new_value)
        top_three.pop(3)
    elif new_value > top_three[1]:
        top_three.insert(1, new_value)
        top_three.pop(3)
    elif new_value > top_three[2]:
        top_three.insert(2, new_value)
        top_three.pop(3)

    return top_three


def run(file_name):
    f = open(file_name, "r")
    elf_cals = 0
    max_elf_cals = 0
    top_three = [0, 0, 0]
    for line in f:
        if line.strip():
            elf_cals += int(line)
        else:
            if elf_cals > max_elf_cals:
                max_elf_cals = elf_cals
            top_three = update_top_three(top_three, elf_cals)
            elf_cals = 0

    if elf_cals > 0:
        if elf_cals > max_elf_cals:
            max_elf_cals = elf_cals
        top_three = update_top_three(top_three, elf_cals)

    print("Day 1 - Part 1: " + str(max_elf_cals))
    print("Day 1 - Part 2: " + str(sum(top_three)))
    f.close()


def run_opt(file_name):
    f = open(file_name, "r")
    all_elves = f.read().split('\n\n')
    each_elf = [[int(x) for x in elf.split("\n")] for elf in all_elves]
    print("Day 1 - Part 1 - Better: " + str(max(sum(elf) for elf in each_elf)))
    sorted_elves = sorted((sum(elf) for elf in each_elf), reverse=True)
    print("Day 1 - Part 2 - Better: " + str(sum(sorted_elves[:3])))
    f.close()

