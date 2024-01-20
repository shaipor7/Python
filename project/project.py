class Tax():
    def __init__(self):
        print("First part: Saving-Insurance Information")
        self.coverage_year = input("Coverage Term (years): ") # 77
        self.payment_year = input("Payment Term (years): ") # 7
        self.payment_amout = input("Payment amount (Bath): ") # 98300
        self.protect_amout = input("assured amount (Bath): ") # 100000
        self.insurance_interest_percentage = input("Cash Benefit per year (percentage): ") # 10
        print("Second part: Personal Information")
        self.age = input("How old are you (years): ") # 24
        self.tax_base_percentage = input("what is your personal tax ? (percentage): ") # 5
        self.reinvestment_interest_percentage = input("What is your expected interest from investment? (percentage): ") # 3

        self.return_money_from_tax = percentage(protect_amout, tax_base_percentage)
        self.return_money_from_insurance = percentage(protect_amout, insurance_interest_percentage)

    def percentage(self, money_amount , percentage):
        return money_amount * percentage / 100

    def accumulate(self):
        total_ivestment_money = 0
        tax_money_back_count = 0
        for ages in range(self.age, self.coverage_year):
            tax_money_back_count =+ 1
            if tax_money_back_count <= self.payment_year:
                total_ivestment_money += reinvestment(self.return_money_from_tax,
                                                    self.reinvestment_interest_percentage,
                                                    self.coverage_year - ages, 1)
            total_ivestment_money += reinvestment(self.return_money_from_insurance,
                                                self.reinvestment_interest_percentage,
                                                self.coverage_year - ages, 1)
        return total_ivestment_money


    def reinvestment(money_amout, interest, year, compounded):
        return money_amout * (1 + interest / compounded) ^ (year * compounded)


def main():
    tax = Tax()
    print(tax.accumulate)

if __name__ == "__main__":
    main()
