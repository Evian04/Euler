"""
The following iterative sequence is defined for the set of positive integers: n → n/2 if n is even, n → 3n + 1 if n is odd.
Find the starting number lower than one million that produces the longest chain.
Note: Once the chain starts the terms are allowed to go above one million.
"""
from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.other_functions import euler_14_sequence

def euler_n14(do_print_result: bool, limit: int = 1000000) -> int:
    time_1 = time_ns()

    longest_chain = 0
    biggest_length = 0
    for i in range(1, limit + 1):
        sequence = euler_14_sequence(i)
        length = len(sequence)

        if length > biggest_length:
            longest_chain = i
            biggest_length = length

        # Since this program is pretty slow (~40 seconds), the following lines of code will show the advancement in % every 10%
        # (only if the variable `do_print_result` is True)
        if do_print_result and i in [n * (limit // 10) for n in range(11)]:
            print(round(i / limit * 100), "%")
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe number lower than {limit} that lead to the longest sequence is: {longest_chain}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")

    return longest_chain

if __name__ == "__main__":
    euler_n14(True)