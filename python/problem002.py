from eulerlib import fibonacci

def calculate() -> str:
    result = sum([x for x in fibonacci(4000000) if x % 2 == 0])
    return str(result)

if __name__ == "__main__":
    print(calculate())
