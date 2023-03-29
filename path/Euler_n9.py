from time import time_ns
from additional_script.accessibility_settings import time_precision

def euler_n9(do_print_result: bool) -> int:
    time_1 = time_ns()

    sum = 1000
    abc = ()

    for a in range(sum):
        for b in range(sum):
            c = sum - a - b

            if c < 0:
                continue

            if a ** 2 + b ** 2 != c ** 2:
                continue

            abc = (a, b, c)
            break

        if abc:
            break

    product = abc[0] * abc[1] * abc[2]
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe only triplet of Pythagoras whose sum = 1000 is: {abc[0]}, {abc[1]} and {abc[2]}")
        print(f"The product of these numbers is: {product}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds")
    
    return product

if __name__ == "__main__":
    euler_n9(True)