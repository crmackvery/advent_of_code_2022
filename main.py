# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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


def read_file(file_name):
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

    print(max_elf_cals)
    print(top_three)
    print(sum(top_three))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file('/Users/chrismack/PycharmProjects/advent_of_code/inputs/day1.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
