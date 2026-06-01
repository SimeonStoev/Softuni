class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if len(email[:email.index("@")]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if email[-4:] not in [".com", ".net", ".org"] and email[-3:] != ".bg":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")