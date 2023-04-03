"""
Find the largest prime factor of the number 600 851 475 143.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision

def euler_n3(do_print_result, number_to_test: int = 600851475143) -> int:
    time_1 = time_ns()

    result = number_to_test
    i = 2

    while True:
        if result % i == 0:
            result //= i

        else:
            i += 1
        
        if i ** 2 > result:
            break

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe biggest prime factor of {number_to_test} is: {result}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)}\n")
    
    return result

if __name__ == "__main__":
    euler_n3(True, 100)