# file_handling_assignment.py

def read_and_write_file(input_file, output_file):
    """
    Reads the content of input_file, modifies it, 
    and writes the modified version into output_file.
    """
    try:
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File '{input_file}' was read and modified version saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def safe_file_read():
    """
    Asks the user for a filename and handles errors gracefully.
    """
    filename = input("\nEnter the filename to read: ")

    try:
        with open(filename, "r") as f:
            print("\n📂 File content:\n")
            print(f.read())
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if _name_ == "_main_":
    print("=== FILE HANDLING ASSIGNMENT ===")

    # Part 1: File Read & Write Challenge
    input_file = "input.txt"
    output_file = "output.txt"
    read_and_write_file(input_file, output_file)

    # Part 2: Error Handling Lab
    safe_file_read()
    
