def main():
    print("First part: Saving-Insurance Information")
    coverage_year = input("Coverage Term (years): ") # 77
    payment_year = input("Payment Term (years): ") # 7
    payment_amout = input("Payment amount at assured 100k Bath (Bath): ") # 98300
    interest_percentage = input("Cash Benefit per year (percentage): ") # 10
    print("Second part: Personal Information")
    age = input("How old are you (years): ")
    tax_base_percentage = input("what is your personal tax ? (percentage): ")

def income_by_insurance(money_amount = 100000, interest_percentage):
    income_per_year = money_amount * interest_percentage / 100
    return income_per_year

def income_by_tax_returning()

def accumulate():
    ...


def reinvestment(money_amout, interest, year, compounded):
    return money_amout * (1 + interest / compounded) ^ (year * compounded)


if __name__ == "__main__":
    main()
