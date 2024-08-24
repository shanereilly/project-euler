numbers: dict[int:str] = {1: "one",
                          2: "two",
                          3: "three", 
                          4: "four",
                          5: "five",
                          6: "six",
                          7: "seven",
                          8: "eight",
                          9: "nine",
                          10: "ten",
                          11: "eleven",
                          12: "twelve",
                          13: "thirteen",
                          14: "fourteen",
                          15: "fifteen",
                          18: "eighteen",
                          20: "twenty",
                          30: "thirty",
                          40: "forty",
                          50: "fifty",
                          60: "sixty",
                          70: "seventy",
                          80: "eighty",
                          90: "ninety",
                          1000: "onethousand"}

def sum_letters_in_numbers(n: int):
    total: int = 0
    for i in range(1, n + 1):
        if i in numbers:
            total += len(numbers[i])
        else:
            if i < 20:
                numbers[i] = numbers[i % 10] + "teen"
                total += len(numbers[i])
            elif i < 100:
                ones: int = i % 10
                tens: int = i - ones
                numbers[i] = numbers[tens] + numbers[ones] 
                total += len(numbers[i])
            elif i < 1000:
                tens: int = i % 100
                hundreds: int = i // 100
                if tens != 0:
                    numbers[i] = numbers[hundreds] + "hundredand" + numbers[tens] 
                else:
                    numbers[i] = numbers[hundreds] + "hundred"
                total += len(numbers[i])
    return total

def calculate() -> str:
    return str(sum_letters_in_numbers(1000))

if __name__ == "__main__":
    print(calculate())
