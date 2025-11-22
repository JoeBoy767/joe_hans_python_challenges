def is_prime(n):
    """Returns True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    num = 120
    print(is_prime(num))


def is_prime(n):
    """Returns True if n is a prime number from a list of numbers, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20]
    for number in test_numbers:
        print(f"{number} is prime: {is_prime(number)}")


def is_prime(n):
    """Returns True if n is a prime number, else False. Accepts user input."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    input_number = int(input("Enter a number to check if it's prime: "))
    print(f"{input_number} is prime: {is_prime(input_number)}")
