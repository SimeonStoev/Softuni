def validate_password(password):
    valid_password = True
    has_diff_symbols = False
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        valid_password = False
    digits = 0
    for character in password:
        if character.isdigit():
            digits += 1
        if ord(character) not in range(65, 91) and ord(character) not in range(97, 123) and not character.isdigit() and not has_diff_symbols:
            valid_password = False
            has_diff_symbols = True
            print("Password must consist only of letters and digits")

    if digits < 2:
        valid_password = False
        print("Password must have at least 2 digits")

    if valid_password:
        print("Password is valid")

passw = input()
validate_password(passw)