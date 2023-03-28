from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.other_functions import is_palindrome

def euler_n4(do_print_result: bool) -> int:
    time_1 = time_ns()

    biggest_palindrome = 1
    ab = ()

    for a in range(1000):
        for b in range(1000):
            product = a * b

            if is_palindrome(str(product)):
                if product > biggest_palindrome:
                    biggest_palindrome = product
                    ab = (a, b)
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nHere is the biggest palindrome that can be written as the product of two 3-digits integers: {biggest_palindrome}")
        print(f"The product that lead to this number is: {ab[0]} x {ab[1]}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return biggest_palindrome