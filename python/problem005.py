from math import lcm
def calculate() -> str:
    result = lcm(*range(2,21))
    return str(result)

if __name__ == "__main__":
    print(calculate())
