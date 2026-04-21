MAX_ATTEMPTS = 3
PASSWORD = "python123"


def check_password_strength(pwd):
    """Basic password strength checker"""
    if len(pwd) < 6:   #checking for password length; less than 6
        return "Weak"
    elif pwd.isalpha() or pwd.isdigit():   #checking if password is only letters or digits
        return "Medium"
    elif any(char.isdigit() for char in pwd) and any(char.isalpha() for char in pwd): 
        return "Strong"  #checking if atleast a letter or digit is present in the password
    else:
        return "Very Strong"


def validate_input(user_input):
    """Validate user input"""
    if not user_input:
        raise ValueError("Password cannot be empty")
    if len(user_input.strip()) == 0:
        raise ValueError("Invalid input (only spaces)")
    return user_input


for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        user_input = input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter password: ")

        # Validate input
        user_input = validate_input(user_input)

        # Check strength (for learning/demo purposes)
        strength = check_password_strength(user_input)
        print(f"Password strength: {strength}")

        if user_input == PASSWORD:
            print("Access granted")
            break
        else:
            print("Wrong password")

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)

else:
    print("Access denied")