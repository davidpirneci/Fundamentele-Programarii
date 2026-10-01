import math

def check_prime(n:int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_twin_primes(n: int) -> tuple[int, int]:
    current = n + 1
    while True:
        if check_prime(current) and check_prime(current + 2):
            return current, current + 2
        current += 1

n = int(input("Enter a non-null natural number: "))
p,q = find_twin_primes(n)

print(f"The first twin prime numbers immediately larger than {n} are {p} and {q}")

