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
def read_user_input():
    try:
        with open(filename, mode='r') as f:
            file_content = f.readlines()
            for line in file_content:
                print(line.rstrip('\n'))
    except (IOError, IndexError):
        pass
    finally:
        print('Cleanup!')
read_user_input()

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
import pickle
import json
filename_pickle = "user_input.pickle"  # Name of the file to write the input using pickle
filename_json = "user_input.json"  # Name of the file to write the input using JSON
def listen_user_input():
    user_input_list = []
    waiting_for_input = True
    while waiting_for_input:
        print('Please choose')
        print('1: Add a new input:')
        print('q: Quit')
        user_input = get_user_choice()
        if user_input == '1':
            user_info = input('Enter your input: ')
            user_input_list.append(user_info)
        elif user_input == 'q':
            waiting_for_input = False
        else:
            print('Invalid input, please try again.')

    # Writing the list to a file using pickle
    with open(filename_pickle, "wb") as file:
        pickle.dump(user_input_list, file)

    # Writing the list to a file using JSON
    with open(filename_json, "w") as file:
        json.dump(user_input_list, file)

    print("Input saved.")

listen_user_input()

# 4) Adjust the logic to load the file content to work with pickled/ json data.
def read_file_content():
    try:
        # Reading pickled data from file
        with open(filename_pickle, "rb") as file:
            pickle_data = pickle.load(file)
            print("Pickled data:", pickle_data)

        # Reading JSON data from file
        with open(filename_json, "r") as file:
            json_data = json.load(file)
            print("JSON data:", json_data)

    except FileNotFoundError:
        print("File not found.")

read_file_content()
