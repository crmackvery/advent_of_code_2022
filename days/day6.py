
def find_index_of_non_repeat(message, length_to_check):
    index = 0
    for idx, char in enumerate(message[length_to_check:]):
        found = True
        for c in message[idx:idx+length_to_check]:
            if message[idx:idx+length_to_check].count(c) > 1:
                found = False
                break

        if found:
            index = idx + length_to_check
            break

    return index


def run_pt1_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 6 - Part 1: " + str(find_index_of_non_repeat(f.read(), 4)))
    f.close()


def run_pt2_first_pass(file_name):
    f = open(file_name, "r")
    print("Day 6 - Part 2: " + str(find_index_of_non_repeat(f.read(), 14)))
    f.close()