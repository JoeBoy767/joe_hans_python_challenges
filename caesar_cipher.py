def caesar_cipher(text, shift):
    """Encrypts the input text using a Caesar cipher with the specified shift."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char

    return result
if __name__ == "__main__":
    sample_text = "Hello, World!"
    shift_value = 3
    encrypted_text = caesar_cipher(sample_text, shift_value)
    print("Encrypted text:", encrypted_text)


def caesar_cipher(text, shift):
    """Encrypts the input text using a Caesar cipher with the specified shift, then saves to file."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
    return result

def save_to_file(filename, content):
    """Save content to a file with basic error handling."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Message saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving file: {e}")
save_to_file("encrypted_message.txt", encrypted_text)

if __name__ == "__main__":
    # User input
    """Allows for user input of text and shift value, then saves the encoded message to a file."""
    text = input("Enter text to encode: ")
    try:
        shift = int(input("Enter shift value (can be negative or large): "))
    except ValueError:
        print("Shift must be an integer.")
        exit(1)

    encoded = caesar_cipher(text, shift)
    print("\nEncoded message:")
    print(encoded)

    # Save to file
    save_to_file("encoded.txt", encoded)


def caesar_decrypt(ciphertext, shift):
    """Decrypts a Caesar cipher by shifting letters backward."""
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift backward for decryption
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char

    return plaintext
if __name__ == "__main__":
    encrypted_message = "Khoor, Zruog!"
    shift_value = 3
    decrypted_message = caesar_decrypt(encrypted_message, shift_value)
    print("Decrypted text:", decrypted_message)
