from time import time_ns
from additional_script.accessibility_settings import time_precision

def euler_n2(do_print_result: bool) -> int:
    time_1 = time_ns()

    sequence = [1, 2]
    sum = 1

    while sequence[-1] < 4000000:
        if sequence[-1] % 2 == 0:
            sum += sequence[-1]

        sequence.append(sequence[-1] + sequence[-2])

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe obtained number is: {sum}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n2(True)