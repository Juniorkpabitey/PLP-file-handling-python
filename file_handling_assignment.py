# File Creation
try:
    # Open file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 67890\n")
        print("File created and initial content written successfully.")
except Exception as e:
    # Handle any exceptions that may occur during file creation
    print("Error occurred during file creation:", e)
finally:
    # Clean up code, executed regardless of whether an exception occurred or not
    print("File creation process completed.")

# File Reading and Display
try:
    # Open file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    # Handle FileNotFoundError
    print("Error: File not found.")
except PermissionError:
    # Handle PermissionError
    print("Error: Permission denied.")
except Exception as e:
    # Handle any other exceptions
    print("Error occurred during file reading:", e)

# File Appending
try:
    # Open file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("This is line 4, appended.\n")
        file.write("78901\n")
        file.write("Appending another line with text and numbers: 23456\n")
        print("Content appended successfully.")
except Exception as e:
    # Handle any exceptions that may occur during file appending
    print("Error occurred during file appending:", e)

# Error Handling using try, except, and finally blocks
try:
    # Code that might raise exceptions
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    # Handle FileNotFoundError
    print("Error: File not found.")
except PermissionError:
    # Handle PermissionError
    print("Error: Permission denied.")
except Exception as e:
    # Handle any other exceptions
    print("Error occurred:", e)
finally:
    # Clean up code, executed regardless of whether an exception occurred or not
    print("Error handling demonstration completed.")
