def is_prime(x):
    x = int(x)
    for i in range(2, x):
        if (x % i) == 0:
            x = False
        else:
            x = True
    return x

def counter(n):
    count = 0
    for num in range(2, n + 1):
        if is_prime(num):
            count += 1
    return count

try:
    user_input = int(input("Enter a positive integer: "))
    if user_input < 0:
        print("Please enter a positive integer.")
    else:
        prime_count = counter(user_input)
        print(f"There are {prime_count} prime numbers up to {user_input}.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")