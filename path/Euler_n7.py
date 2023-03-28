from time import time_ns

from additional_script.prime_related_functions import get_next_prime

prime = 1

for _ in range(10001):
    prime = get_next_prime(prime)

print(f"The 10'001th is: {prime}")