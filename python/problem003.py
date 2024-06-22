from eulerlib import smallest_prime_factor

def calculate() -> str:
    x : int = 600851475143
    y : int
    while x != (y := smallest_prime_factor(x)):
        x //= y
    result = x
    return str(result)

if __name__ == "__main__":
    print(calculate())
