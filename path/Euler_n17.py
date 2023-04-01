"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""
from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.other_functions import get_letters

def euler_n17(do_print_result: bool, limit: int = 1000) -> int:
    time_1 = time_ns()

    all_letters = ""
    for i in range(1, limit + 1):
        all_letters += get_letters(i)
    
    total_letters = len(all_letters.replace(" ", ""))
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe total letters it takes to write all the integers between 1 and {limit} is: {total_letters}\n")
        print(f"Comuting time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return total_letters

if __name__ == "__main__":
    euler_n17(True)