"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision
from additional_files.other_functions import is_palindrome

def euler_n4(do_print_result: bool, range_of_ab: int = 1000) -> int:
    time_1 = time_ns()

    biggest_palindrome = 1
    ab = ()

    for a in range(range_of_ab):
        for b in range(range_of_ab):
            product = a * b

            if is_palindrome(str(product)):
                if product > biggest_palindrome:
                    biggest_palindrome = product
                    ab = (a, b)
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe biggest palindrome that can be written as the product of two integers smaller than {range_of_ab} is: {biggest_palindrome}")
        print(f"The product that lead to this number is: {ab[0]} x {ab[1]}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return biggest_palindrome

if __name__ == "__main__":
    euler_n4(True)