def is_palindrome(n: str) -> bool:
    for i in len(n) // 2:
        if n[i] != n[-i - 1]:
            return False
    
    return True