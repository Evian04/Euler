def is_palindrome(n: str) -> bool:
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            return False
    
    return True

def get_triangle(n: int) -> int:
    sum = 0

    for i in range(n + 1):
        sum += n
    
    return sum