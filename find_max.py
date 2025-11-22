def find_max(numbers):
    """Returns the maximum number from a list of numbers. Includes mixed positive and negative numbers."""
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
if __name__ == "__main__":
    sample_numbers = [-10, 0, 5, 3, 99, -5]
    print("The maximum number is:", find_max(sample_numbers))


def find_max(numbers):
    """Returns the maximum number from a list of numbers. Has error handling for empty lists."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
if __name__ == "__main__":
    sample_numbers = []
    print("The maximum number is:", find_max(sample_numbers))