"""
Find how many routes are there through a 20x20 grid by starting at the top-left corner,
finishing at the top right corner, and only being able to go right or down.
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision

def euler_n15(do_print_result: bool, grid_size: int = 20) -> int:
    time_1 = time_ns()

    graph = [[1]]
    diagonals = (grid_size + 1) * 2 - 1
    for d in range(1, diagonals):
        previous_diagonal = graph[d - 1]
        
        if d / diagonals < 0.5:
            current_diagonal = [0 for p in range(len(previous_diagonal) + 1)]

            for i in range(len(current_diagonal)):
                if i == 0:
                    current_diagonal[i] = previous_diagonal[i]
                    continue

                if i == len(current_diagonal) - 1:
                    current_diagonal[i] = previous_diagonal[i - 1]
                    break

                current_diagonal[i] = previous_diagonal[i - 1] + previous_diagonal[i]

        else:
            current_diagonal = [0 for p in range(len(previous_diagonal) - 1)]

            for i in range(len(current_diagonal)):
                current_diagonal[i] = previous_diagonal[i] + previous_diagonal[i + 1]
            
        graph.append(current_diagonal)
    
    routes = graph[-1][0]

    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe number of possible routes through a {grid_size}x{grid_size} grid is: {routes}\n")
        print(f"Comuting time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return routes

if __name__ == "__main__":
    euler_n15(True)