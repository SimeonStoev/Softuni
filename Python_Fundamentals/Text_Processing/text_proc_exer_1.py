def is_username_valid(user: str) -> bool:
    if 3 > len(user) or len(user) > 16:
        return False

    for char in user:
        if not char.isalpha() and not char.isdigit() and char not in ("-", "_"):
            return False

    if user != " ".join(user.split()):
        return False
    
    return True


usernames = input().split(", ")

for username in usernames:
    if is_username_valid(username):
        print(username)
