def calculate() -> str:
    result = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
    return str(result)

if __name__ == "__main__":
    print(calculate())
