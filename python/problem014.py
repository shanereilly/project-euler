prev_collatz = {}

def collatz_len(start: int) -> int:
    n: int = start
    length : int = 1
    while n != 1:
        if n in prev_collatz:
            prev_collatz[start] = length + prev_collatz[n]
            return length + prev_collatz[n]
        else:
            length += 1
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
    prev_collatz[start] = length
    return length

def max_collatz(limit: int) -> int:
    max_collatz : int = 0
    max_collatz_start : int = 0
    for i in range(1, limit):
        n : int = collatz_len(i)
        if n > max_collatz:
            max_collatz = n
            max_collatz_start = i
    return max_collatz_start

def calculate() -> str:
    return str(max_collatz(1000000))

if __name__ == "__main__":
    print(calculate())
