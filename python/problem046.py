from typing import Generator
from eulerlib import generate_primes

def generate_twice_squares() ->Generator[int,None,None]:
    n: int = 0
    while True:
        yield 2 * (n ** 2)
        n += 1

def calculate() -> str:
    primes: list[int] = []
    primeset: set[int] = set()
    prime_gen = generate_primes()
    primes.append(next(prime_gen))
    primeset.add(primes[-1])

    squareset: set[int] = set()
    square_gen = generate_twice_squares()
    curr_square: int = next(square_gen)
    squareset.add(curr_square)

    n: int = 9

    while True:
        n += 2
        while primes[-1] < n:
            primes.append(next(prime_gen))
            primeset.add(primes[-1])
        while curr_square < n:
            curr_square = next(square_gen)
            squareset.add(curr_square)
        if n not in primeset:
            found: bool = True
            for prime in primes:
                if n < prime:
                    break
                if n - prime in squareset:
                    found = False
                    break
            if found:
                return str(n)

if __name__ == "__main__":
    print(calculate())
