from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.prime_related_functions import get_prime_scope

def euler_n10(do_print_result: bool, limit: int = 2000000) -> int:
    time_1 = time_ns()

    list_primes = get_prime_scope(2, limit)
    
    sum = 0
    for prime in list_primes:
        sum += prime
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe sum of all the prime numbers below {limit} is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n10(True)