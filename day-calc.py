#!/usr/bin/env python3

import os
import datetime
from curtsies.fmtfuncs import green, bold, blue, red, cyan
from tkinter import *
from tkinter import messagebox

days_passed = 0
os.system("clear")
now = datetime.datetime.now()


def day_passed_gui():
    window = Tk()
    window.title("Days passed")
    window.geometry("600x100")
    window.configure(background="gray")
    label = Label(window, text="Enter date in format MM-DD-YYYY: ", bg="gray")
    label.config(font=("Arial", 10))
    label.grid(column=0, row=0)
    entry = Entry(window, width=30)
    entry.config(font=("Arial", 10))
    entry.grid(column=1, row=0)
    button = Button(window, text="Submit", command=lambda: day_passed_submit_gui(entry))
    button.config(font=("Arial", 10))
    button.grid(column=1, row=1)
    label2 = Label(window, text="Current date and time : ", bg="gray")
    label2.config(font=("Arial", 10))
    label2.grid(column=0, row=3)
    label3 = Label(window, text=now.strftime("%m-%d-%Y"), bg="gray")
    label3.config(font=("Arial", 10))
    label3.grid(column=1, row=3)
    window.mainloop()


def day_passed_submit_gui(entry):
    user_input = entry.get()
    user_input = datetime.datetime.strptime(user_input, "%m-%d-%Y")
    day_input = now - user_input
    messagebox.showinfo("Days passed", "Days passed: " + str(day_input.days))
    weeks_passed = day_input.days / 7
    messagebox.showinfo("Weeks passed", "Weeks passed: " + str(weeks_passed))
    months_passed = day_input.days / 30
    messagebox.showinfo("Months passed", "Months passed: " + str(months_passed))
    years_passed = day_input.days / 365
    messagebox.showinfo("Years passed", "Years passed: " + str(years_passed))
    exit(0)


def day_passed_cli():
    print(green(bold("Welcome to the date calculator!")))
    print(blue(bold("Please enter a date in the format MM-DD-YYYY")))
    user_input = input()
    user_input = datetime.datetime.strptime(user_input, "%m-%d-%Y")
    day_input = now - user_input
    print(red(bold("Days passed: " + str(day_input.days))))
    weeks_passed = day_input.days / 7
    print(cyan(bold("Weeks passed: " + str(weeks_passed))))
    months_passed = day_input.days / 30
    print(cyan(bold("Months passed: " + str(months_passed))))
    years_passed = day_input.days / 365
    print(cyan(bold("Years passed: " + str(years_passed))))
    print(blue(bold("Do you want to enter another date? Enter y for yes or n for no")))
    user_input = input()
    if user_input == "y":
        day_passed_cli()
    elif user_input == "n":
        exit(0)
    else:
        exit(0)


def gui_or_cli():
    print(blue(bold("Do you want to use the GUI? y/n?: ")))
    user_input = input()
    if user_input == "y":
        day_passed_gui()
    elif user_input == "n":
        day_passed_cli()
    else:
        exit(0)


gui_or_cli()
