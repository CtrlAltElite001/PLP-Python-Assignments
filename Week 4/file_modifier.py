import os

def modify_content(content):
    """
    Function to modify file content.
    For example, converting all text to uppercase.
    """
    return content.upper()

# Main Program
try:
    # Ask the user for input filename
    input_file = input("Enter the filename to read: ")

    # Always look inside the same folder as this script
    script_dir = os.path.dirname(__file__)   # folder where file_modifier.py is located
    file_path = os.path.join(script_dir, input_file)

    # Open and read the file
    with open(file_path, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Save the modified version with "modified_" prefix in the same folder
    output_file = os.path.join(script_dir, "modified_" + input_file)
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"File successfully modified and saved as '{output_file}'")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
