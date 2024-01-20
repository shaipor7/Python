def main():
    print("First part: Saving-Insurance Information")
    coverage_year = input("Coverage Term (years): ") # 77
    payment_year = input("Payment Term (years): ") # 7
    payment_amout = input("Payment amount (Bath): ") # 98300
    protect_amout = input("assured amount (Bath): ") # 100000
    insurance_interest_percentage = input("Cash Benefit per year (percentage): ") # 10
    print("Second part: Personal Information")
    age = input("How old are you (years): ")
    tax_base_percentage = input("what is your personal tax ? (percentage): ")
    reinvestment_interest_percentage = input("What is your expected interest from investment? (percentage): ")

    return_money_from_tax = percentage(protect_amout, tax_base_percentage)
    return_money_from_insurance = percentage(protect_amout, insurance_interest_percentage)

    money_from_reinvestment = reinvestment(return_money_from_tax + return_money_from_insurance,
                                           reinvestment_interest_percentage, coverage_year - age,
                                           1)
    

def percentage(money_amount , percentage):
    return money_amount * percentage / 100

def accumulate():
    ...


def reinvestment(money_amout, interest, year, compounded):
    return money_amout * (1 + interest / compounded) ^ (year * compounded)


if __name__ == "__main__":
    main()
