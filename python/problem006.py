from eulerlib import square_of_sums, sum_of_squares

def calculate() -> str:
    result = abs(square_of_sums(100) - sum_of_squares(100))
    return str(result)

if __name__ == "__main__":
    print(calculate())
