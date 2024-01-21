class Tax():
    def __init__(self):
        print("*****************************************")
        print("First part: Saving-Insurance Information")
        print("*****************************************")
        self.coverage_year = 77 #int(input("Coverage Term (years): ")) # 77
        self.payment_year =  7#int(input("Payment Term (years): ")) # 7
        self.payment_amout = 100000#int(input("Payment amount (Bath): ")) # 98300
        self.protect_amout = 100000#int(input("assured amount (Bath): ")) # 100000
        self.insurance_interest_percentage = 10 #int(input("Cash Benefit per year (percentage): ")) # 10
        print("*****************************************")
        print("Second part: Personal Information")
        print("*****************************************")
        self.tax_base_percentage = 20 #int(input("what is your personal tax ? (percentage): ")) # 5
        self.reinvestment_interest_percentage = 1.5 #float(input("What is your expected interest from investment? (percentage): ")) # 3

        self.return_money_from_tax = self.percentage(self.protect_amout, self.tax_base_percentage)
        self.return_money_from_insurance = self.percentage(self.protect_amout, self.insurance_interest_percentage)

        self.total = self.accumulate()

    def __str__(self):
        return str(self.total)

    def percentage(self, money_amount , percentage):
        return money_amount * percentage / 100

    def income_tax_accumulate(self):
        total_investment_money = 0
        tax_money_back_count = 0
        for ages in range(self.coverage_year):
            tax_money_back_count += 1
            if tax_money_back_count <= self.payment_year:
                total_investment_money += self.reinvestment(self.return_money_from_tax,
                                                    self.reinvestment_interest_percentage,
                                                    self.coverage_year - ages, 1)
            total_investment_money += self.reinvestment(self.return_money_from_insurance,
                                                self.reinvestment_interest_percentage,
                                                self.coverage_year - ages, 1)
        return total_investment_money
    def income_invest_accumulate(self):


    def reinvestment(self, money_amout, interest, year, compounded):
        return money_amout * (1 + interest / 100 / compounded) ** (year * compounded)


def main():
    tax = Tax()
    print(tax)

if __name__ == "__main__":
    main()
