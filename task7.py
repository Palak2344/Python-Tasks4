def read_file(filename):
    """Open and read a text file, printing its content line by line."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Print each line without extra whitespace
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the filename
filename = 'sample.txt'

# Call the function to read the file
read_file(filename)
