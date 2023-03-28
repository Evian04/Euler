from time import time_ns
from additional_script.prime_related_functions import get_next_prime
from additional_script.accessibility_settings import time_precision

def euler_n7(do_print_result: bool) -> int:
    time_1 = time_ns()

    prime = 1

    for _ in range(10001):
        prime = get_next_prime(prime)

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe 10 001 th prime is: {prime}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return prime