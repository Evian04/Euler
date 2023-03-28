from time import time_ns

time_1 = time_ns()

sequence = [1, 2]
sum = 1

while sequence[-1] < 4000000:
    if sequence[-1] % 2 == 0:
        sum += sequence[-1]

    sequence.append(sequence[-1] + sequence[-2])

time_2 = time_ns()

print(f"\nThe obtained number is: {sum}\n")

print(f"Computing time: {round((time_2 - time_1) / 10**9, 8)} seconds\n")