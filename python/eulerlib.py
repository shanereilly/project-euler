from math import isqrt
from typing import Generator

def fibonacci(n: int) -> Generator[int,None,None]:
    x = 0
    y = 1
    while x <= n:
        yield x
        x, y = y, x + y

def generate_primes() -> Generator[int,None,None]:
    D = {}
    q : int = 2
    while True:
        # Is prime.
        if q not in D:
            yield q
            D[q*q] = q
        ## Is not prime.
        else:
            p : int = D[q] + q
            while p in D:
                p += D[q]
            D[p] = D[q]
            del D[q]
        q += 1

def is_palindrome(n: int) -> bool:
    return n == reverse_number(n)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, isqrt(n + 1)):
        if n % i == 0:
            return False
    return True
        
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
