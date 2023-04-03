"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision

def euler_n2(do_print_result: bool, limit: int = 4000000) -> int:
    time_1 = time_ns()

    sequence = [1, 2]
    sum = 0

    while sequence[-1] < limit:
        if sequence[-1] % 2 == 0:
            sum += sequence[-1]

        sequence.append(sequence[-1] + sequence[-2])

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe sum of the even numbers of the Fibonacci sequence that are smaller than {limit} is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n2(True)