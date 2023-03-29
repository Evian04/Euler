from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.constants import const_grid

def euler_n11(do_print_result: bool, grid: list[list[int]] = []) -> int:
    time_1 = time_ns()
    if not grid:
        grid = const_grid
    
    biggest_product = 0
    index = ()

    for i in range(len(grid) - 3):
        for j in range(len(grid[0]) - 3):
            product = 1

            for increment in range(4):
                product *= grid[i + increment][j + increment]
            
            if product > biggest_product:
                biggest_product = product
                index = (i, j)
    
    numbers = ", ".join([str(grid[index[0] + i][index[1] + i]) for i in range(4)])

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe biggest product of four numbers diagonally adjacent is: {biggest_product}")
        print(f"The four numbers in question are: {numbers}")
        print(f"The index of the beginning of this sequence is: {index[0]}, {index[1]}")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return biggest_product

if __name__ == "__main__":
    euler_n11(True)