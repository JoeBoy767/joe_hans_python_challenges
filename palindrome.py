def is_palindrome():
    """Reads a string from user input and checks if it is a palindrome."""
    user_input = input("Enter a string: ")
    cleaned_input = ''.join(user_input.split()).lower()
    if cleaned_input == cleaned_input[::-1]:
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')
if __name__ == "__main__":
    is_palindrome()
