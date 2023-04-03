"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision
from additional_files.other_functions import is_leap

def euler_n19(do_print_result: bool, day_to_check = "Sunday") -> int:
    time_1 = time_ns()

    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day_per_month = {m: d for m in all_months for d in [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]}

    total = 0

    total_days = 2
    day = 1         # 1 -> 28, 29, 30 or 31
    month = 0       # 0 -> 11
    year = 1901     # 1901 -> 2000

    while year != 2000 or month != 11 or day != 31:
        if day == 1 and all_days[total_days % 7] == day_to_check:
            total += 1
        
        day += 1
        total_days += 1

        if day == 29 and all_months[month] == "Feb" and is_leap(year):
            continue

        if day > day_per_month[all_months[month]]:
            day = 1
            month += 1

        if month == 12:
            month = 0
            year += 1
    
    time_2 = time_ns()
    
    if do_print_result:
        print(f"\nThe number of Sunday which fell on the first of the month during the twentieth century is: {total}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")

if __name__ == "__main__":
    euler_n19(True)