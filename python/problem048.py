def calculate() -> str:
    total: int = 0
    for i in range(1, 1001):
        total %= 10_000_000_000 
        total += pow(i, i, 10_000_000_000)
    return str(total)

if __name__ == "__main__":
    print(calculate())
