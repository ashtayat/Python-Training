with open('Exercise-6/numbers.txt', 'w') as file:
    # Write numbers from 1 to 10, each on a new line
    for number in range(1, 11):
        file.write(f'{number}\n')

print("Numbers from 1 to 10 have been written to numbers.txt")