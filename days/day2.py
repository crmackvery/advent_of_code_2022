points = {"X": 1, "Y": 2, "Z": 3}
results = {"X": 0, "Y": 3, "Z": 6}

full_result = {"A X": points["X"] + 3, "A Y": points["Y"] + 6, "A Z": points["Z"] + 0,
               "B X": points["X"] + 0, "B Y": points["Y"] + 3, "B Z": points["Z"] + 6,
               "C X": points["X"] + 6, "C Y": points["Y"] + 0, "C Z": points["Z"] + 3}

p2_result = {"A X": results["X"] + points["Z"], "A Y": results["Y"] + points["X"], "A Z": results["Z"] + points["Y"],
             "B X": results["X"] + points["X"], "B Y": results["Y"] + points["Y"], "B Z": results["Z"] + points["Z"],
             "C X": results["X"] + points["Y"], "C Y": results["Y"] + points["Z"], "C Z": results["Z"] + points["X"]}


def run_pt1(file_name):
    f = open(file_name, "r")
    print("Day 2 - Part 1: " + str(sum(full_result[x] for x in f.read().split("\n"))))
    f.close()


def run_pt2(file_name):
    f = open(file_name, "r")
    print("Day 2 - Part 2: " + str(sum(p2_result[x] for x in f.read().split("\n"))))
    f.close()
