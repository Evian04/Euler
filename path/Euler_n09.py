from time import time_ns
from additional_script.accessibility_settings import time_precision

def euler_n9(do_print_result: bool) -> int:
    time_1 = time_ns()

    sum = 1000
    abc = ()

    for a in range(1, sum):
        for b in range(1, sum):
            c = sum - a - b

            if c < 0:
                continue

            if a > b or b > c:
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
        print(f"\nThe product of The only triplet of Pythagoras whose sum = 1000 is: {product}")
        print(f"The triplet in question: {abc[0]}, {abc[1]} and {abc[2]}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds")
    
    return product

if __name__ == "__main__":
    euler_n9(True)