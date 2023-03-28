from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.prime_related_functions import get_prime_decomp

def euler_n5(do_print_result: int) -> int:
    time_1 = time_ns()

    upper_limit = 20

    numbers_to_test = range(2, upper_limit + 1)
    product = 1

    for number in numbers_to_test:
        product_copy = product

        for prime in get_prime_decomp(number):
            if product_copy % prime == 0:
                product_copy //= prime
            
            else:
                product *= prime
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe lowest integer that can be divided by all the numbers between 1 and {upper_limit} is: {product}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds")
    
    return product

euler_n5(True)