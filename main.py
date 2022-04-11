# using tkinter + python to create a simple kickboxing-class-generator
from tkinter import *
from random import choice
import smtplib
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox


def generate_class():
    level = level_combo.get()
    rounds = round_entries.get()
    email = email_entry.get()
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

    if len(level) == 0 or len(rounds) == 0 or len(email) == 0:
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

        send_email(final_rounds, email)
        # reminder - delete entries


def difficult_level(level):
    if level == "advance":
        return 8
    elif level == "intermediate":
        return 6
    else:
        return 4


def send_email(rounds, email_address):
    pass
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

email_label = Label(text="Which email should we send the class? ", bg="white")
email_label.config(font=p_font, padx=5, pady=5)
email_label.grid(column=2, row=5)

# Entries
round_entries = Entry(width=32, bg="white")
round_entries.config(font=p_font)
round_entries.grid(column=3, row=3)

email_entry = Entry(width=32, bg="white")
email_entry.config(font=p_font)
email_entry.grid(column=3, row=5)

# Dropdown options
level_combo = Combobox(width=30, text="select the level...", justify="center", values=["Advance", "Intermediate", "Beginner"])
level_combo.config(font=p_font, state="readonly")
level_combo.grid(column=3, row=4)

# Buttons
class_generate_button = Button(text="Generate Kickboxing Class", bg="white", command=generate_class)
class_generate_button.config(font=p_font, pady=10)
class_generate_button.grid(column=2, columnspan=3, row=6)

window.mainloop()