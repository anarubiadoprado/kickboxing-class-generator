# using tkinter + python to create a simple kickboxing-class-generator

# creating functions I will need
from random import choice


def generate_class(level, rounds):
    moves = ["jab",
             "cross",
             "hook",
             "modify-cross",
             "lead upper-cut",
             "rear upper-cut",
             "lead front kick",
             "rear front kick",
             "lead round kick",
             "rear round kick"
             ]

    difficult = difficult_level(level)
    final_rounds = []

    while rounds != 0:
        combo = []
        for _ in range(difficult):
            combo.append(choice(moves))

        # make sure we don't get repeated combos in the same class
        if combo not in final_rounds:
            final_rounds.append(combo)
            rounds -= 1

    return final_rounds


def difficult_level(level):
    if level == "advance":
        return 8
    elif level == "intermediate":
        return 6
    else:
        return 4


final_round = generate_class("advance", 3)
print(final_round)
