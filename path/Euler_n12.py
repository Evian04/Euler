from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.other_functions import get_triangle


def euler_n12(do_print_result: bool, divisors_limit: int = 500) -> int:
    time_1 = time_ns()

    n = 1
    triangle = get_triangle(n)
    while True:
        triangle = get_triangle(n)

        divisors = []
        for i in range(1, triangle + 1):
            if triangle % i == 0:
                divisors.append(i)
        
        if len(divisors) > divisors_limit:
            break

        n += 1
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe first triangle number to have over {divisors_limit} divisors is: {triangle}")
        print(f"This is the triangle number of the number: {n}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")

    return triangle

if __name__ == "__main__":
    euler_n12(True)