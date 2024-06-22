from math import lcm

def reduce_list(ns: list[int]) -> list[int]:
    if 0 in ns:
        ns.remove(0)
    if 1 in ns:
        ns.remove(1)
    reduced_list : list[int] = ns.copy()
    for i in ns:
        for j in ns:
            if i * j in ns:
                if i in reduced_list:
                    reduced_list.remove(i)
                if j in reduced_list:
                    reduced_list.remove(j)
    return reduced_list

def calculate() -> str:
    ns : list[int] = reduce_list(list(range(2,21)))
    result = lcm(*ns)
    return str(result)

if __name__ == "__main__":
    print(calculate())
