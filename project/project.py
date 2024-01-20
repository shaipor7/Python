class Tax():
    def __init__(self):
        print("*****************************************")
        print("First part: Saving-Insurance Information")
        print("*****************************************")
        self.coverage_year = input("Coverage Term (years): ") # 77
        self.payment_year = input("Payment Term (years): ") # 7
        self.payment_amout = input("Payment amount (Bath): ") # 98300
        self.protect_amout = input("assured amount (Bath): ") # 100000
        self.insurance_interest_percentage = input("Cash Benefit per year (percentage): ") # 10
        print("*****************************************")
        print("Second part: Personal Information")
        print("*****************************************")
        self.age = input("How old are you (years): ") # 24
        self.tax_base_percentage = input("what is your personal tax ? (percentage): ") # 5
        self.reinvestment_interest_percentage = input("What is your expected interest from investment? (percentage): ") # 3

        self.return_money_from_tax = self.percentage(self.protect_amout, self.tax_base_percentage)
        self.return_money_from_insurance = self.percentage(self.protect_amout, self.insurance_interest_percentage)

        self.total = self.accumulate()

    def __str__():
        return self.total

    def percentage(self, money_amount , percentage):
        return int(money_amount) * float(percentage) / 100

    def accumulate(self):
        total_investment_money = 0
        tax_money_back_count = 0
        for ages in range(self.age, self.coverage_year):
            tax_money_back_count =+ 1
            if tax_money_back_count <= self.payment_year:
                total_investment_money += self.reinvestment(self.return_money_from_tax,
                                                    self.reinvestment_interest_percentage,
                                                    self.coverage_year - ages, 1)
            total_investment_money += self.reinvestment(self.return_money_from_insurance,
                                                self.reinvestment_interest_percentage,
                                                self.coverage_year - ages, 1)
        return total_investment_money


    def reinvestment(self, money_amout, interest, year, compounded):
        return float(money_amout) * (1 + float(interest) / int(compounded)) ^ (int(year) * int(compounded))


def main():
    tax = Tax()
    print(tax)

if __name__ == "__main__":
    main()
