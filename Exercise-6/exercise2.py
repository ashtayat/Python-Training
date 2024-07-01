with open('Exercise-6/user_input.txt', 'a') as file:
    while True:
        # Ask the user for input
        user_input = input("Enter something (type 'stop' to end): ")
        
        # Check if the user entered 'stop'
        if user_input.lower() == 'stop':
            break
        
        # Append the input to the file
        file.write(f'{user_input}\n')

print("User inputs have been written to user_input.txt")