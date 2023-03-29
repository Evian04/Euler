"""
What is the 10 001st prime number?
"""
from time import time_ns
from additional_script.prime_related_functions import get_next_prime
from additional_script.accessibility_settings import time_precision

def euler_n7(do_print_result: bool, prime_n: int = 10001) -> int:
    time_1 = time_ns()

    prime = 1

    for _ in range(prime_n):
        prime = get_next_prime(prime)

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe {prime_n}th prime is: {prime}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return prime

if __name__ == "__main__":
    euler_n7(True)