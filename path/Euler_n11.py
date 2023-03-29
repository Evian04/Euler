"""
Find the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
in the 20 x 20 grid (the `const_grid` variable).
"""
from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.constants import const_grid

def euler_n11(do_print_result: bool, grid: list[list[int]] = []) -> int:
    time_1 = time_ns()
    if not grid:
        grid = const_grid
    
    biggest_product = 0
    index = ()
    direction = ()

    for i in range(len(grid) - 3):
        for j in range(len(grid[0]) - 3):
            for d in [(0, 1), (1, 0), (1, 1)]:
                product = 1

                for increment in range(4):
                    product *= grid[i + increment * d[0]][j + increment * d[1]]
                
                if product > biggest_product:
                    biggest_product = product
                    index = (i, j)
                    direction = d
    
    numbers = ", ".join([str(grid[index[0] + i * direction[0]][index[1] + i * direction[1]]) for i in range(4)])

    if direction == (0, 1): direction = "right"
    
    elif direction == (1, 0): direction = "down"
    
    else: direction = "diagonal"

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe biggest product of four numbers adjacent is: {biggest_product}")
        print(f"The four numbers in question are: {numbers}")
        print(f"The index of the beginning of this sequence is: {index} and its direction is: {direction}")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return biggest_product

if __name__ == "__main__":
    euler_n11(True)