from math import isqrt
from typing import Generator

def fibonacci(n: int) -> Generator[int,None,None]:
    x = 0
    y = 1
    while x <= n:
        yield x
        x, y = y, x + y

def is_palindrome(n: int) -> bool:
    return n == reverse_number(n)
        
def reverse_number(n: int) -> int:
    negative : bool = False
    x : int = 0
    if n < 0:
        n *= -1
        negative = True
    while n > 0:
        x *= 10
        x += n % 10
        n //= 10
    if negative:
        x *= -1
    return x

def smallest_prime_factor(n: int) -> int:
    assert n >= 2
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i
    # If nothing is found, n is prime. 
    return n

def square_of_sums(n: int) -> int:
     return sum(range(n+1)) ** 2

def sum_of_squares(n: int) -> int:
    return sum([x**2 for x in range(n+1)])
