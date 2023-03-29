"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
What is the value of the first triangle number to have over five hundred divisors?
"""
from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.other_functions import get_divisors


def euler_n12(do_print_result: bool, divisors_limit: int = 500) -> int:
    time_1 = time_ns()

    n = 1
    triangle = n
    while True:
        divisors = get_divisors(triangle)
        
        if len(divisors) > divisors_limit:
            break

        n += 1
        triangle += n
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe first triangle number to have over {divisors_limit} divisors is: {triangle}")
        print(f"It has {len(divisors)} divisors")
        print(f"This is the triangle number of the number: {n}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")

    return triangle

if __name__ == "__main__":
    euler_n12(True)