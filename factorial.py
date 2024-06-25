def factorial(n: int) -> int:
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)

def list_factorial(numbers: list[int]) -> list[int]:
    return [factorial(n) for n in numbers]
print("Module  with functions 'factorial' and 'list_factorial' has been created.")