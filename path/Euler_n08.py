"""
Find the thirteen adjacent digits in the 1000-digit number (the `const_digits` variable) that have the greatest product.
What is the value of this product?
"""
from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.constants import const_digits


def euler_n8(do_print_result: bool, digits: str = "", adjacent_digits: int = 13) -> int:
    time_1 = time_ns()

    if not digits:
        digits = const_digits
        
    biggest_product = 0
    index_biggest_product = 0

    for i in range(len(digits) - adjacent_digits):
        five_digits = [int(d) for d in digits[i:i+adjacent_digits]]
        product = 1

        for d in five_digits:
            product *= d
        
        if product > biggest_product:
            biggest_product = product
            index_biggest_product = i

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe biggest product found in this sequence is: {biggest_product}")
        print(f"index corresponding: {index_biggest_product}")
        print(f"sequence corresponding: \"{digits[index_biggest_product:index_biggest_product+5]}\"\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return index_biggest_product

if __name__ == "__main__":
    euler_n8(True)