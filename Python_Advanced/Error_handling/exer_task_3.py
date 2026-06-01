import re


class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    pattern = re.search(r"^([A-Za-z]+|[0-9]+|[@*&%]+)$", password)
    if pattern:
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    pattern = re.search(r".*[@*&%]+.*", password)
    if not pattern:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    pattern = re.search(r".*\s.*", password)
    if pattern:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")