def is_valid(ticket: str) -> bool:
    return len(ticket) == 20


def get_occurs_of_symbol(ticket: str, character: str) -> int:
    total_occurs = 0
    curr_occurs = 0
    for char in ticket:
        if char == character:
            curr_occurs += 1
        else:
            if total_occurs < curr_occurs:
                total_occurs = curr_occurs
            curr_occurs = 0

    return max(total_occurs, curr_occurs)


tickets = [elem.strip() for elem in input().split(",")]

for ticket in tickets:
    if is_valid(ticket):
        if get_occurs_of_symbol(ticket[:10], "$") == get_occurs_of_symbol(ticket[10:], "$") == 10:
            print(f'ticket "{ticket}" - 10$ Jackpot!')
        elif get_occurs_of_symbol(ticket[:10], "@") == get_occurs_of_symbol(ticket[10:], "@") == 10:
            print(f'ticket "{ticket}" - 10@ Jackpot!')
        elif get_occurs_of_symbol(ticket[:10], "#") == get_occurs_of_symbol(ticket[10:], "#") == 10:
            print(f'ticket "{ticket}" - 10# Jackpot!')
        elif get_occurs_of_symbol(ticket[:10], "^") == get_occurs_of_symbol(ticket[10:], "^") == 10:
            print(f'ticket "{ticket}" - 10^ Jackpot!')
        elif get_occurs_of_symbol(ticket[10:], "$") >= 6 and get_occurs_of_symbol(ticket[:10], "$") >= 6:
            print(
                f'ticket "{ticket}" - {min(get_occurs_of_symbol(ticket[:10], "$"), get_occurs_of_symbol(ticket[10:], "$"))}$')
        elif get_occurs_of_symbol(ticket[10:], "@") >= 6 and get_occurs_of_symbol(ticket[:10], "@") >= 6:
            print(
                f'ticket "{ticket}" - {min(get_occurs_of_symbol(ticket[:10], "@"), get_occurs_of_symbol(ticket[10:], "@"))}@')
        elif get_occurs_of_symbol(ticket[10:], "#") >= 6 and get_occurs_of_symbol(ticket[:10], "#") >= 6:
            print(
                f'ticket "{ticket}" - {min(get_occurs_of_symbol(ticket[:10], "#"), get_occurs_of_symbol(ticket[10:], "#"))}#')
        elif get_occurs_of_symbol(ticket[10:], "^") >= 6 and get_occurs_of_symbol(ticket[:10], "^") >= 6:
            print(
                f'ticket "{ticket}" - {min(get_occurs_of_symbol(ticket[:10], "^"), get_occurs_of_symbol(ticket[10:], "^"))}^')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")
