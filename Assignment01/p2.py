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

def find_goldbach_primes(n: int) -> tuple[int, int] | None:
    if n <= 3:
        return None

    for p1 in range(2, (n//2)+1):
        if check_prime(p1):
            p2=n-p1
            if check_prime(p2):
                return p1, p2
    return None

n = int(input("Enter a natural number n: "))
result = find_goldbach_primes(n)

if result:
    p1, p2 = result
    print(f"{n} can be written as the sum of two prime numbers: {p1}+{p2}")
else:
    print("No prime pair found")