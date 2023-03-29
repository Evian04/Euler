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