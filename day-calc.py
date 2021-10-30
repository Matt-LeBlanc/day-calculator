#!/usr/bin/env python3

import os
import datetime
from curtsies.fmtfuncs import green, bold, blue, cyan
from tkinter import *
from tkinter import messagebox
import json

days_passed = 0
os.system("clear")
now = datetime.datetime.now()
global save_date


# add a class to store different dates
class Date:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day

    # add a method to store different dates
    def save_date(self):
        date_dict = self.name, self.year, self.month, self.day
        with open('save_date.json', 'w') as f:
            json.dump(date_dict, f, indent=4)


def day_passed_gui():
    window = Tk()
    window.title("Days passed")
    window.geometry("550x100")
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
    entry.focus()
    window.bind('<Return>', lambda event: day_passed_submit_gui(entry))
    window.mainloop()


def day_passed_submit_gui(entry):
    global save_date
    user_input = entry.get()
    user_input = datetime.datetime.strptime(user_input, "%m-%d-%Y")
    save_date = user_input
    save_date_list = save_date.strftime("%m-%d-%Y")
    print(save_date_list)
    with open("save_date.json", "w") as f:
        json.dump(save_date_list, f)
    day_input = now - user_input
    messagebox.showinfo("Days passed", "Days passed: " + str(day_input.days))
    weeks_passed = day_input.days / 7
    messagebox.showinfo("Weeks passed", "Weeks passed: " + str(weeks_passed))
    months_passed = day_input.days / 30
    messagebox.showinfo("Months passed", "Months passed: " + str(months_passed))
    years_passed = day_input.days / 365
    messagebox.showinfo("Years passed", "Years passed: " + str(years_passed))
    exit()


def day_passed_cli():
    global save_date
    print(green(bold("Welcome to the date calculator!")))
    print(cyan(bold("Please enter a date in the format MM-DD-YYYY")))
    user_input = input()
    user_input = datetime.datetime.strptime(user_input, "%m-%d-%Y")
    save_date = user_input
    save_date_list = save_date.strftime("%m-%d-%Y")
    print(save_date_list)
    with open("save_date.json", "w") as f:
        json.dump(save_date_list, f)
    calculate_days(user_input)


def gui_or_cli():
    print(blue(bold("Do you want to use the GUI? y/n?: ")))
    user_input = input()
    if user_input == "y":        day_passed_gui()
    elif user_input == "n":
        day_passed_cli()
    else:
        exit()


def calculate_days(date):
    date_then = date
    date_now = datetime.datetime.now()
    date_diff = date_now - date_then
    passed = date_diff.days
    weeks_passed = passed / 7
    months_passed = passed / 30
    years_passed = passed / 365
    print(green(bold("Welcome to the date calculator!")))
    print(cyan(bold("Current date : " + now.strftime("%m-%d-%Y"))))
    print(cyan(bold("Saved date : " + save_date.strftime("%m-%d-%Y"))))
    print(cyan(bold("Days passed : " + str(passed))))
    print(cyan(bold("Weeks passed : " + str(weeks_passed))))
    print(cyan(bold("Months passed : " + str(months_passed))))
    print(cyan(bold("Years passed : " + str(years_passed))))


def main():
    global save_date
    if os.path.isfile("save_date.json"):
        with open("save_date.json", "r") as f:
            save_date = json.load(f)
            save_date = datetime.datetime.strptime(save_date, "%m-%d-%Y")
            calculate_days(save_date)
            print(green(bold("Do you want to save another date? y/N?: ")))
            user_input = input()
            if user_input == "y":
                gui_or_cli()
            elif user_input == "n":
                exit()
    else:
        gui_or_cli()


main()
