import math

def check_triples(limit : int) -> int:
    a : int = 1
    b : int = 2
    while True:
        c : int = math.isqrt(a**2 + b**2)
        if (a + b + c > limit):
            a += 1
            b = a + 1
            b += 1
        elif (c**2 != a**2 + b**2) or (a + b + c < limit):
            b += 1
        else:
            return a * b * c

def calculate() -> str:
    return str(check_triples(1000))

if __name__ == "__main__":
    print(calculate())
