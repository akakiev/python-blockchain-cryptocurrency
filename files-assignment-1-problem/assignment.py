# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
filename = 'user_input.txt'
def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input('Your choice: ')
    return user_input
def listen_user_input():
    waiting_for_input = True
    while waiting_for_input:
        print('Please choose')
        print('1: Add a new input:')
        print('q: Quit')
        user_input = get_user_choice()
        if user_input == '1':
            user_info = input('Enter your input: ')
            with open(filename, mode='a') as f:
                f.write(user_info + '\n')
        elif user_input == 'q':
            waiting_for_input = False
        else:
            print('Invalid input, please try again.')
    print("Program completed.")
listen_user_input()
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
# 4) Adjust the logic to load the file content to work with pickled/ json data.
