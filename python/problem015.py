from math import comb

def paths_in_square_lattice(n: int) -> int:
    return comb(n * 2, n)

def calculate() -> str:
    return str(paths_in_square_lattice(20))

if __name__ == "__main__":
    print(calculate())
