from time import time_ns
from additional_script.accessibility_settings import time_precision

def euler_n6(do_print_result: bool) -> int:
    time_1 = time_ns()
    
    first_integers = 10

    sum_of_squares = 0
    for i in range(1, first_integers + 1):
        sum_of_squares += i ** 2
    
    square_of_sum = 0
    for i in range(1, first_integers + 1):
        square_of_sum += i
    square_of_sum **= 2

    difference = square_of_sum - sum_of_squares

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe difference between the square of the sum and the sum of the square is: {difference}\n")
        print(f"Computing time: {round(time_2 - time_1) / 10**9, time_precision} seconds\n")
    
    return difference