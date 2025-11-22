def reverse_string():
    """Reads a string from user input and prints the reversed string."""
    user_input = input("Enter a string: ")
    reversed_string = user_input[::-1]
    print("Reversed string:", reversed_string)
if __name__ == "__main__":
    reverse_string()
