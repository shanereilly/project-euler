from eulerlib import generate_primes

def sum_primes(limit: int) -> int:
    total : int = 0
    primes = generate_primes()
    while((x := next(primes)) < limit):
        total += x
    return total

def calculate() -> str:
    return str(sum_primes(2000000))

if __name__ == "__main__":
    print(calculate())
