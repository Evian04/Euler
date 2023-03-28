def is_prime(n: int) -> bool:
    for i in range(2, round(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    
    return True

def get_next_prime(limit: int) -> int:
    n = limit

    while True:
        n += 1

        if is_prime(n):
            return n

def get_prime_scope(min: int, max: int) -> list:
	scope = []

	for n in range(min, max + 1):
		if is_prime(n):
			scope.append(n)
	
	return scope