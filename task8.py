def write_to_file(filename, data):
    """Write data to a file."""
    with open(filename, 'w') as file:
        file.write(data + '\n')  # Write the user input and add a newline

def append_to_file(filename, additional_data):
    """Append additional data to the file."""
    with open(filename, 'a') as file:
        file.write(additional_data + '\n')  # Append the additional data with a newline

def read_file(filename):
    """Read and display the content of the file."""
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFinal content of the file:")
        print(content)

# Specify the filename
filename = 'output.txt'

# Take user input
user_input = input("Please enter some data to write to the file: ")
write_to_file(filename, user_input)

# Take additional input to append
additional_input = input("Please enter additional data to append to the file: ")
append_to_file(filename, additional_input)

# Read and display the final content of the file
read_file(filename)
