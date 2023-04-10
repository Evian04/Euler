"""
A number is called "abundant" if the sum of its proper divisors is greater than the number itself.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision
from additional_files.other_functions import is_abundant

def euler_n23(do_print_result: bool, limit: int = 28123) -> int:
    time_1 = time_ns()

    list_abundant = []

    for i in range(1, limit + 1):
        if is_abundant(i):
            list_abundant.append(i)

    print("step 1")
    list_sum_non_abundant = list(range(1, limit + 1))
    
    for n1 in list_abundant:
        for n2 in list_abundant:
            if n1 + n2 in list_sum_non_abundant:
                list_sum_non_abundant.remove(n1 + n2)
    
    sum = 0

    for n in list_sum_non_abundant:
        sum += n
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe sum of all the positive integers which cannot be written as the sum of two abundant numbers is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n23(True)