from time import time_ns

time_1 = time_ns()

tested_numbers = []

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        tested_numbers.append(n)

time_2 = time_ns()

print(f"\nHere are all the integers between 1 and 1 000 that are multiple of 3 or 5 :\n{tested_numbers}\n")

print(f"Computing time: {round((time_2 - time_1) / 10**9, 8)} seconds\n")