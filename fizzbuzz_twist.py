# Extended FizzBuzz with Fizz (3), Buzz (5), Bang (7)
for num in range(1, 101):
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    if num % 7 == 0:
        output += "Bang"
    
    # Print the number if none of the rules apply
    print(output or num)


# Extended FizzBuzz with Fizz (3), Buzz (5), Bang (7), and user-defined rules; outputs to file
def get_rules():
    """Prompt the user to enter custom rules for FizzBuzz."""
    rules = {}
    print("Enter your rules (divisor and word). Type 'done' when finished.")
    while True:
        entry = input("Enter rule as 'divisor word': ").strip()
        if entry.lower() == "done":
            break
        try:
            divisor_str, word = entry.split()
            divisor = int(divisor_str)
            if divisor <= 0:
                print("Divisor must be a positive integer.")
                continue
            rules[divisor] = word
        except ValueError:
            print("Invalid format. Example: 3 Fizz")
    return rules

def run_custom_fizzbuzz(rules, start=1, end=100):
    """Run FizzBuzz with user-defined rules and return output as a list of strings."""
    output_lines = []
    for num in range(start, end + 1):
        output = "".join(word for divisor, word in rules.items() if num % divisor == 0)
        output_lines.append(output or str(num))
    return output_lines

def main():
    rules = get_rules()
    if not rules:
        print("No rules provided. Exiting.")
        return

    start, end = 1, 100
    output_lines = run_custom_fizzbuzz(rules, start, end)

    # Display the results
    print("\nCustom FizzBuzz Output:")
    for line in output_lines:
        print(line)

    # Option to save to a file
    save = input("\nDo you want to save the output to a file? (y/n): ").strip().lower()
    if save == "y":
        filename = input("Enter filename (e.g., output.txt): ").strip()
        try:
            with open(filename, "w") as f:
                for line in output_lines:
                    f.write(line + "\n")
            print(f"Output saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()