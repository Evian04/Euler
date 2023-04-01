"""
By starting at the top of the triangle `const_triangle` and moving to adjacent numbers on the row below,
find the maximum sum that can be reached by adding the all the number of a certain path.
"""
from time import time_ns
from additional_script.accessibility_settings import time_precision
from additional_script.constants import const_triangle

def euler_n18(do_print_result: bool, triangle: list[list[int]] = const_triangle) -> int:
    time_1 = time_ns()
    
    depth = len(triangle)

    triangle.reverse()
    added_triangle = [triangle[0]]

    for i in range(1, depth):
        row = []

        for j in range(len(triangle[i])):
            if added_triangle[i - 1][j] > added_triangle[i - 1][j + 1]:
                row.append(triangle[i][j] + added_triangle[i - 1][j])
            
            else:
                row.append(triangle[i][j] + added_triangle[i - 1][j + 1])
        
        added_triangle.append(row)
    
    triangle.reverse()
    added_triangle.reverse()

    best_path = [0]

    for i in range(depth - 1):
        if added_triangle[i + 1][best_path[i]] > added_triangle[i + 1][best_path[i] + 1]:
            best_path.append(best_path[i])
        
        else:
            best_path.append(best_path[i] + 1)
    
    sum = 0

    for i in range(len(best_path)):
        sum += triangle[i][best_path[i]]
    
    best_path = ", ".join([
        "left" * (best_path[i] == best_path[i + 1]) + "right" * (best_path[i] != best_path[i + 1]) for i in range(depth - 1)
    ])
    
    time_2 = time_ns()

    if do_print_result:
        print(f"\nThe higher sum possible is: {sum}")
        print(f"The path that lead to this sum is: {best_path}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum

if __name__ == "__main__":
    euler_n18(True)