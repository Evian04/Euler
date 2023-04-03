"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision

def euler_n1(do_print_result: bool, limit: int = 1000) -> list[int]:
    time_1 = time_ns()

    tested_numbers = []

    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            tested_numbers.append(n)

    sum = 0
    for n in tested_numbers:
        sum += n

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe sum of all the integers between 1 and {limit} that are multiple of 3 or 5 is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n1(True)