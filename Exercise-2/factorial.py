def factorial(n: int) -> int:
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def list_factorial(l):
    return [factorial(n) for n in l]


print(list_factorial([1,2,3,4,5]))