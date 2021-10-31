#!/usr/bin/env python3

import os
import datetime
from curtsies.fmtfuncs import green, bold, cyan
import json

days_passed = 0
os.system("clear")
now = datetime.datetime.now()
global save_date, save_date_dir
save_date_dir = f"/home/" + os.getlogin() + "/"


def day_passed():
    global save_date, save_date_dir
    print(green(bold("Welcome to the date calculator!")))
    print(cyan(bold("Please enter a date in the format MM-DD-YYYY")))
    user_input = input()
    user_input = datetime.datetime.strptime(user_input, "%m-%d-%Y")
    save_date = user_input
    save_date_list = save_date.strftime("%m-%d-%Y")
    print(save_date_list)
    with open(f"{save_date_dir}day_calculator.json", "w") as f:
        json.dump(save_date_list, f)
    calculate_days(user_input)


def calculate_days(date):
    global save_date, save_date_dir
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
    global save_date, save_date_dir
    if os.path.isfile(f"{save_date_dir}day_calculator.json"):
        with open(f"{save_date_dir}day_calculator.json", "r") as f:
            save_date = json.load(f)
            save_date = datetime.datetime.strptime(save_date, "%m-%d-%Y")
            calculate_days(save_date)
            print(green(bold("Do you want to save another date? y/N?: ")))
            user_input = input()
            if user_input == "y":
                day_passed()
            elif user_input == "n":
                exit()
    else:
        day_passed()


if __name__ == "__main__":
    main()
