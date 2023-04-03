from math import isqrt

def is_palindrome(n: str) -> bool:
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            return False
    
    return True

def get_divisors(n: int) -> list[int]:
    divisors = []

    for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                divisors.append(i)

                if n // i != i:
                    divisors.append(n // i)
    
    return divisors

def euler_14_sequence(n: int) -> list[int]:
    sequence = [n]

    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        
        else:
            sequence.append(sequence[-1] * 3 + 1)
    
    return sequence

def get_letters(n: int) -> str:
    number_to_letters = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    in_letters = ""
    
    if n >= 10 ** 12:
        print("Error function `path.additional_files.other_functions.get_letters()` : the given number is too big (bigger than a thousand billion)")
        return ""

    if n >= 10 ** 9:
        separator = len(str(n)) - 9
        return get_letters(int(str(n)[:separator])) + " billion " + get_letters(int(str(n)[separator:]))
    
    if n >= 10 ** 6:
        separator = len(str(n)) - 6
        return get_letters(int(str(n)[:separator])) + " million " + get_letters(int(str(n)[separator:]))
    
    if n >= 10 ** 3:
        separator = len(str(n)) - 3

        if str(n)[-3] == "0" and (str(n)[-1] != "0" or str(n)[-2] != "0"):
            print(n)
            return get_letters(int(str(n)[:separator])) + " thousand and " + get_letters(int(str(n)[separator:]))
        
        return get_letters(int(str(n)[:separator])) + " thousand " + get_letters(int(str(n)[separator:]))
    
    if n >= 10 ** 2:
        if str(n)[1] != "0" or str(n)[2] != "0":
            return get_letters(int(str(n)[0])) + " hundred and " + get_letters(int(str(n)[1:]))
        
        return get_letters(int(str(n)[0])) + " hundred " + get_letters(int(str(n)[1:]))

    if n >= 20:
        return number_to_letters[(n // 10) * 10] + " " + number_to_letters[n % 10]
    
    if n >= 0:
        return number_to_letters[n]
    
    print("Error function `path.additional_files.other_functions.get_letters()` : the given number cannot be negative")

def is_leap(year: int) -> bool:
    if year % 4 != 0 or year % 400 == 0:
        return False
    
    return True

def factorial(n: int) -> int:
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

def sum_of_divisors(n: int) -> int:
    divisors = get_divisors(n)

    if len(divisors) != 1:
        divisors.pop(1)
    
    sum = 0

    for d in divisors:
        sum += d

    return sum

def get_related_amicable(n: int) -> int:
    related_n = sum_of_divisors(n)

    if sum_of_divisors(related_n) == n and related_n != n:
        return related_n

    return 0