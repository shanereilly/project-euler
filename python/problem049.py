from eulerlib import prime_sieve

def is_permutation(n1: int, n2: int) -> bool:
    return sorted(str(n1)) == sorted(str(n2))

def calculate() -> str:
    primes = [prime for prime in prime_sieve(9999) if prime > 999]
    primeset = set(primes)
    for i in range(len(primes) - 2):
        for j in range(i + 1, len(primes) - 1):
            diff: int = (primes[j] - primes[i]) + primes[j]
            if (diff in primeset and 
                is_permutation(primes[i], primes[j]) and
                is_permutation(primes[i], diff) and
                primes[i] != 1487
               ):
                return str(primes[i]) + str(primes[j]) + str(diff)

if __name__ == "__main__":
    print(calculate())
