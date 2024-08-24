
def sum_exponent_digits(base: int, exponent: int) -> int:
    return sum(int(x) for x in list(str(pow(base, exponent))))

def calculate() -> str:
    return str(sum_exponent_digits(2,1000))

if __name__ == "__main__":
    print(calculate())
