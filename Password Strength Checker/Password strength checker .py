import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)

print(f"Password Strength: {strength}")