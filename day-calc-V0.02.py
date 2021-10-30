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


    def load_date(self):
        with open('save_date.json', 'r') as f:
            date_dict = json.load(f)
        self.name = date_dict[0]
        self.year = date_dict[1]
        self.month = date_dict[2]
        self.day = date_dict[3]
        return self.name, self.year, self.month, self.day

    def modify_date(self):
        with open('save_date.json', 'r') as f:
            date_dict = json.load(f)
            print(date_dict)
        choice = input("Which date do you want to modify? ")
        if choice == "name":
            choice = input("Do you want to modify the name? ")
            if choice == "yes":
                name = input("What is the new name? ")
                self.name = name
                date_dict.pop(choice)
                date_dict.update({choice: self.name})
                with open('save_date.json', 'w') as f:
                    json.dump(date_dict, f, indent=4)
            elif choice == "no":
                choice = input("Do you want to remove the date from the list? ")
                if choice == "yes":
                    date_dict.pop(choice)
                    with open('save_date.json', 'w') as f:
                        json.dump(date_dict, f, indent=4)
                elif choice == "no":
                    print("No changes made.")


    def calc_days(self):
        global days_passed
        days_passed = (now - datetime.datetime(self.year, self.month, self.day)).days
        return days_passed

    def print_date(self):
        print(f"{days_passed} days have passed since {self.name}")



def main():
    global days_passed
    date_list = []
    while True:
        print(f"{green(bold(blue('Date Calculator')))}")
        print(f"{green('1. Add a date')}")
        print(f"{green('2. Modify a date')}")
        print(f"{green('3. Calculate days passed since a date')}")
        print(f"{green('4. Exit')}")
        choice = input("What do you want to do? ")
        if choice == "1":
            date_name = input("What is the name of the date? ")
            date_year = int(input("What year is the date? "))
            date_month = int(input("What month is the date? "))
            date_day = int(input("What day is the date? "))
            date_list.append(Date(date_name, date_year, date_month, date_day))
            date_list[-1].save_date()
            print("Date added.")
        elif choice == "2":
            date_list[-1].modify_date()
        elif choice == "3":
            date_list[-1].calc_days()
            date_list[-1].print_date()
        elif choice == "4":
            break
        else:
            print("No such choice.")



if __name__ == "__main__":
    main()
