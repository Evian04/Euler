"""
Find the sum of the digits of the number 2 ** 1000
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision

def euler_n16(do_print_result: bool, n: int = 2 ** 1000) -> int:
    time_1 = time_ns()

    digits = [int(d) for d in str(n)]

    sum = 0
    for d in digits:
        sum += d
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe sum of the digits of this number is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n16(True)