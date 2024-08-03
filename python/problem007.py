from itertools import islice

from eulerlib import generate_primes

def calculate() -> str:
    result = next(islice(generate_primes(), 10000, None))
    return str(result)

if __name__ == "__main__":
    print(calculate())
