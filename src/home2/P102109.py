
def maximum(m:int) -> int:

    max = 0
    numbers = []

    for i in range(m):
        n = int(input("Adj meg egy egész számot: "))
        numbers.append(n)

    for i in numbers:
        if i > max:
            max = i

    return max

print(maximum(6))