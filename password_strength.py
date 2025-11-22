import string

def check_password_strength(password):
    """Check password strength and indicate missing requirements."""
    missing = []

    # Criteria checks
    if len(password) < 8:
        missing.append("Minimum 8 characters")
    if not any(c.isupper() for c in password):
        missing.append("Need at least one uppercase letter")
    if not any(c.islower() for c in password):
        missing.append("Need at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        missing.append("Need at least one number")
    if not any(c in string.punctuation for c in password):
        missing.append("Need at least one symbol")

    # Determine strength
    if len(missing) == 0:
        strength = "Strong"
    elif len(missing) <= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, missing


def suggest_password(password, missing_requirements):
    """Return a suggestion to improve the password."""
    suggestion = password
    for req in missing_requirements:
        if "uppercase" in req:
            suggestion += "A"
        elif "lowercase" in req:
            suggestion += "a"
        elif "number" in req:
            suggestion += "1"
        elif "symbol" in req:
            suggestion += "!"
        elif "Minimum 8 characters" in req:
            suggestion += "X" * (8 - len(password))
    return suggestion

if __name__ == "__main__":
    while True:
        user_password = input("Enter a password to check: ")
        strength, missing_requirements = check_password_strength(user_password)

        print(f"Password Strength: {strength}")
        if missing_requirements:
            print("Missing requirements:")
            for req in missing_requirements:
                print(f" - {req}")
            suggestion = suggest_password(user_password, missing_requirements)
            print(f"Suggested improvement: {suggestion}")
        else:
            print("Your password is strong!")
            break