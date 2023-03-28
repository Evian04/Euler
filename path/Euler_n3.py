from time import time_ns
from additional_script.prime_related_functions import get_prime_scope
from additional_script.accessibility_settings import time_precision

def euler_n3(do_print_result) -> int:
    time_1 = time_ns()

    number_to_test = 600851475143 # 600 851 475 143
    i = number_to_test // 2

    primes = get_prime_scope(2, number_to_test // 2)
    primes.reverse()

    print("scope got")

    for prime in primes:
        if number_to_test % prime == 0:
            biggest_prime = prime

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe biggest prime factor of {number_to_test} is: {biggest_prime}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)}\n")
    
    return biggest_prime