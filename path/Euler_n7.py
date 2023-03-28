from time import time_ns
from additional_script.prime_related_functions import get_next_prime

time_1 = time_ns()

prime = 1

for _ in range(10001):
    prime = get_next_prime(prime)

time_2 = time_ns()

print(f"The 10 001 th prime is: {prime}")
print(f"Computing time: {round((time_2 - time_1) / 10**9, 8)} seconds\n")