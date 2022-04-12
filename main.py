# using tkinter + python to create a simple kickboxing-class-generator
from random import choice
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox

# it generate the kickboxing class
def generate_class():
    level = level_combo.get()
    rounds = round_entries.get()
    # all moves that we usually use in class
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
    # makes sure the user has filled the field, otherwise pop alert
    if len(level) == 0 or len(rounds) == 0:
        messagebox.showinfo(title="Oops", message="Please, make sure you haven't left any field empty!")
    else:
        rounds = int(rounds)
        difficult = difficult_level(level.lower())
        final_rounds = []

        while rounds != 0:
            combo = []
            for _ in range(difficult):
                combo.append(choice(moves))

            # make sure we don't get repeated combos in the same class
            if combo not in final_rounds:
                final_rounds.append(combo)
                rounds -= 1

        create_file(final_rounds)


def difficult_level(level):
    if level == "advance":
        return 8
    elif level == "intermediate":
        return 6
    else:
        return 4


# ideally I want to set up to send a email with the kickboxing class, but for simplicity, it will create a file

def create_file(rounds):

    count = 1
    file = "Your personally designed kickboxing class!\n"
    for rd in rounds:
        sentences = ""
        for r in rd:
            sentences += f"{r} | "
        file += f"Round {count}: {sentences} \n"
        count += 1

    file1 = open("kickboxing-class.txt", "w")
    file1.write(file)

    messagebox.showinfo(title="Yay!", message="Your file kickboxing-class was create. Your class is ready!")
    clear()

# clear the fields
def clear():
    round_entries.delete(0, END)
    level_combo.set('')

# ----------- UI Setup -------------#


window = Tk()
window.title("Kickboxing Class Generator")
window.config(padx=50, pady=50, bg="white")
title_font = Font(family="Helvetica", size=24, weight="bold")
p_font = Font(family="Helvetica", size=12)
canvas = Canvas(width=500, height=600, bg="white", highlightthickness=0)

# Labels
app_label = Label(text="Kickboxing Class Generator", bg="white")
app_label.config(font=title_font, padx=5, pady=5)
app_label.grid(column=2, columnspan=3, row=1)

round_label = Label(text="How many rounds?", bg="white")
round_label.config(font=p_font, padx=5, pady=5)
round_label.grid(column=2, row=3)

level_label = Label(text="Select the level of difficult", bg="white")
level_label.config(font=p_font, padx=5, pady=5)
level_label.grid(column=2, row=4)

# Entries
round_entries = Entry(width=32, bg="white")
round_entries.config(font=p_font)
round_entries.grid(column=3, row=3)

# Dropdown options
level_combo = Combobox(width=30, text="select the level...", justify="center",
                       values=["Advance", "Intermediate", "Beginner"])
level_combo.config(font=p_font, state="readonly")
level_combo.grid(column=3, row=4)

# Buttons
class_generate_button = Button(text="Generate Kickboxing Class", bg="white", command=generate_class)
class_generate_button.config(font=p_font, pady=10)
class_generate_button.grid(column=2, columnspan=3, row=6)

window.mainloop()
