"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
Find the sum of all the amicable numbers under 1000.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision
from additional_files.other_functions import get_related_amicable

def euler_n21(do_print_result: bool, limit: int = 10000) -> int:
    time_1 = time_ns()

    list_amicable_n = []

    for i in range(2, limit):
        related_i = get_related_amicable(i)

        if related_i == 0:
            continue

        if i in list_amicable_n:
            continue

        list_amicable_n.append(i)
        list_amicable_n.append(related_i)
    
    sum = 0

    for amicabe_n in list_amicable_n:
        sum += amicabe_n
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe sum of all the amicable numbers under 1000 is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n21(True)