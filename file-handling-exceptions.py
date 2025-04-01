filename = "C:/Users/Test/OneDrive/Desktop/Plp_Codes/python/week_4/sample.txt"
output_filename = "C:/Users/Test/OneDrive/Desktop/Plp_Codes/python/week_4/modified_sample.txt"

def read_and_modify_file(input_filename, output_filename):
    """Reads a file, modifies the content, and writes to a new file."""
    try:
        with open(input_filename, "r") as file:
            content = file.read()
        
        modified_content = content.upper()

        with open(output_filename, "w") as file:
            file.write(modified_content)

        print(f"File processed successfully. Output saved in '{output_filename}'.")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You don't have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_modify_file(filename, output_filename)
