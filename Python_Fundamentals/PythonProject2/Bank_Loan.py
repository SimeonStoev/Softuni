def calc_monthly_payment(sum, montly_percent, number_of_installemtns):
    montly_payment = sum * ((montly_percent * pow(1 + montly_percent, number_of_installemtns)
                             ) / (pow(1 + montly_percent, number_of_installemtns) - 1))

    return montly_payment


def get_monthly_payment_info():
    print("Sum:")
    sum = float(input())
    print("Interest rate percent:")
    year_percent = float(input())
    print("Period in months:")
    number_of_installments = int(input())

    year_percent /= 100
    monthly_payment = calc_monthly_payment(
        sum, year_percent / 12, number_of_installments)

    print(
        f"Montly payment {monthly_payment:.2f}")

    sum_principal = 0
    sum_interest = 0

    for i in range(1, number_of_installments + 1):
        monthly_payment = calc_monthly_payment(
            sum, year_percent / 12, number_of_installments - i + 1)
        interest_rate = sum * (year_percent / 12)
        principal = monthly_payment - interest_rate
        print(
            f"Month {i}: Interest - {interest_rate:.2f}, Principal - {principal:.2f}")

        sum -= principal
        sum_principal += principal
        sum_interest += interest_rate

    print(f"principal: {sum_principal:.2f}")
    print(f"interest : {sum_interest:.2f}")


def get_credit_payment_info():
    print("Sum:")
    sum = float(input())
    print("Interest rate percent:")
    year_percent = float(input())
    year_percent /= 100
    print("Period in months:")
    number_of_installments = int(input())
    print("Sum to give to loan every month:")
    sum_to_save = float(input())
    print("Insurance for loan:")
    insurance = float(input())

    year_sum_to_principal = 0

    sum_left = sum
    month = 0

    monthly_payment = calc_monthly_payment(
        sum, year_percent / 12, number_of_installments) + insurance

    year_sum_to_principal = sum_to_save - monthly_payment

    print(f"Sum to save every month: {year_sum_to_principal:.2f}")

    year_sum_to_principal *= 12

    sum_principal = 0
    sum_interest = 0
    years = 0

    while sum_left > 0:
        month += 1
        interest_rate = sum_left * (year_percent / 12)
        principal = monthly_payment - interest_rate
        print(
            f"Month {month}: Interest - {interest_rate:.2f}, Principal - {principal:.2f}")

        sum_left -= principal

        if month % 12 == 0:
            extra = min(year_sum_to_principal, sum_left)
            sum_left -= extra
            sum_principal += extra
            years += 1

        sum_principal += principal
        sum_interest += interest_rate

    print(f"Montly payment without insurance: {monthly_payment - insurance:.2f}")
    print(f"Montly payment with insurance: {monthly_payment:.2f}")
    print(f"months: {month}")
    print(f"years: {years}, months: {month % 12}")
    print(f"principal: {sum_principal:.2f}")
    print(f"interest : {sum_interest:.2f}")
    print(f"interest rate: {year_percent * 100:.2f}%")


def get_monthly_payment_info_for_whole_period():
    print("Sum:")
    sum = float(input())
    print("Interest rate percent:")
    year_percent = float(input())
    print("Period in months:")
    number_of_installments = int(input())
    # print("Sum to pay for principal per year:")
    # year_sum_to_principal = float(input())

    year_percent /= 100
    monthly_payment = calc_monthly_payment(
        sum, year_percent / 12, number_of_installments)
    print(f"Montly payment in the beginning {monthly_payment:.2f}")
    sum_principal = 0
    sum_interest = 0

    for i in range(1, number_of_installments + 1):
        interest_rate = sum * (year_percent / 12)
        principal = monthly_payment - interest_rate
        print(
            f"Month {i}: Interest - {interest_rate:.2f}, Principal - {principal:.2f}")

        if i % 12 == 0:
            year_extra_payment_money = (1440 - monthly_payment) * 12
            extra = min(year_extra_payment_money, sum)
            sum -= extra
            sum_principal += extra
            monthly_payment = calc_monthly_payment(
                sum, year_percent / 12, number_of_installments - i + 1)
            print(
                f"Monthly payment adter extra payment: {monthly_payment:.2f}")

        sum -= principal
        sum_principal += principal
        sum_interest += interest_rate

        if monthly_payment == 0:
            break

    print(f"Montly payment: {monthly_payment:.2f}")
    print(f"principal: {sum_principal:.2f}")
    print(f"interest : {sum_interest:.2f}")


get_credit_payment_info()
