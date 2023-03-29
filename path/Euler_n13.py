"""
Find the first ten digits of the sum of the following one-hundred 50-digit numbers (the `const_list_50_digits_numbers` variable).
"""
from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.constants import const_list_50_digits_numbers

def euler_n13(do_print_result: bool, list_numbers: list[int] = []) -> str:
    time_1 = time_ns()

    if not list_numbers:
        list_numbers = const_list_50_digits_numbers
    
    sum = 0
    for n in list_numbers:
        sum += n
    
    ten_first_digits = str(sum)[:10]

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe ten first digits of the sum of these numbers are: {ten_first_digits}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return ten_first_digits

if __name__ == "__main__":
    euler_n13(True)