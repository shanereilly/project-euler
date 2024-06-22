from eulerlib import is_palindrome

def calculate() -> str:
    largest : int = 0
    for i in [x * y for x in range(100,999) for y in range(100,999)]:
        if is_palindrome(i) and i > largest:
            largest = i
    result = largest
    return str(result)

if __name__ == "__main__":
    print(calculate())
