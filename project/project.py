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

    total_ivestment_money = accumulate()

def percentage(money_amount , percentage):
    return money_amount * percentage / 100

def accumulate(payment_year):
    total_ivestment_money = 0
    tax_money_back_count = 0
    for ages in range(age, coverage_year):
        tax_money_back_count =+ 1
        if tax_money_back_count <= payment_year:
            total_ivestment_money += reinvestment(return_money_from_tax, reinvestment_interest_percentage,
                                                  coverage_year - ages, 1)
        total_ivestment_money += reinvestment(return_money_from_insurance, reinvestment_interest_percentage,
                                                  coverage_year - ages, 1)
    return total_ivestment_money


def reinvestment(money_amout, interest, year, compounded):
    return money_amout * (1 + interest / compounded) ^ (year * compounded)


if __name__ == "__main__":
    main()
