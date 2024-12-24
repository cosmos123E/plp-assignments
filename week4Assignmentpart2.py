def read_file_with_error_handling():
    filename = input("Please enter the filename: ")
    
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_file_with_error_handling()
