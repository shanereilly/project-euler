from math import isqrt
from typing import Generator

def generate_triangle_numbers() -> Generator[int, None, None]:
    n : int = 1
    total: int = n
    while True:
        yield total
        n += 1
        total += n

def count_divisors(n: int) -> int:
    total: int = 0
    for i in range(1, isqrt(n)):
        if n % i == 0:
            total += 2
    if isqrt(n) ** 2 == n:
        total + 1
    return total

def count_triangle_divisors(n: int) -> int:
    triangles = generate_triangle_numbers()
    curr: int = next(triangles)
    while (count_divisors(curr) < n):
        curr: int = next(triangles)
    return curr

def calculate() -> str:
    return str(count_triangle_divisors(500))

if __name__ == "__main__":
    print(calculate())
