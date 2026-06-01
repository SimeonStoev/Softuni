class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = input().split(", ")
balance = float(balance)
age = int(age)

while True:
    command = input()
    if command == "End":
        break

    command = command.split("#")
    if command[0] == "Send Money":
        c_money = float((command[1]))
        c_pin_code = command[2]
        if c_money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if c_pin_code != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= c_money
        print(f"Successfully sent {c_money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")
    elif command[0] == "Receive Money":
        c_money = float((command[1]))
        if c_money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        balance += c_money / 2
        print(f"{(c_money / 2):.2f} money went straight into the bank account")
