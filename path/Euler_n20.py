"""
Find the sum of the digits of the number 100!.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision
from additional_files.other_functions import factorial

def euler_n20(do_print_result: bool, n: int = 0) -> int:
    time_1 = time_ns()

    if n == 0:
        n = 100
    
    f = factorial(n)

    sum = 0

    for d in str(f):
        sum += int(d)
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe sum of the digits of the factorial of the number {n} is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n20(True)