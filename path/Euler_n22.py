"""
By working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
Find the total of all the name scores in the file?
"""
from time import time_ns
from additional_files.accessibility_settings import time_precision
from pathlib import Path

def euler_n22(do_print_result: bool) -> int:
    time_1 = time_ns()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    with open(Path(__file__).parent / "additional_files\\names.txt", "rt") as file:
        list_names = file.read()[1:-1]
    
    list_names = list_names.split("\",\"")
    sum_scores = 0
    
    for i in range(len(list_names)):
        score = 0
        for l in list_names[i]:
            score += alphabet.find(l) + 1
        
        sum_scores += score * (i + 1)
    
    time_2 = time_ns()
    
    if do_print_result:
        print(f"\nThe total of all the scores of the names is: {sum_scores}\n")
        print(f"Computing time: {round((time_2 - time_1) / 10**9, time_precision)} seconds\n")
    
    return sum_scores

if __name__ == "__main__":
    euler_n22(True)