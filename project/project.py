class Tax():
    def __init__(self):
        # print("*****************************************")
        # print("First part: Saving-Insurance Information")
        # print("*****************************************")
        self.coverage_year = 52 #int(input("Coverage Term (years): ")) # 77
        self.payment_year =  7 #int(input("Payment Term (years): ")) # 7
        self.payment_amout = 100000#int(input("Payment amount (Bath): ")) # 98300
        self.protect_amout = 100000#int(input("assured amount (Bath): ")) # 100000
        self.final_return_money = 700000 #int(input("Final return money (Bath): ")) #700000
        self.insurance_interest_percentage = 10 #int(input("Cash Benefit per year (percentage): ")) # 10
        # print("*****************************************")
        # print("Second part: Personal Information")
        # print("*****************************************")
        self.tax_base_percentage = 5 #int(input("what is your personal tax ? (percentage): ")) # 5
        self.reinvestment_interest_percentage = 3 #float(input("What is your expected interest from investment? (percentage): ")) # 3

        self.return_money_from_tax = self.percentage(self.protect_amout, self.tax_base_percentage)
        self.return_money_from_insurance = self.percentage(self.protect_amout, self.insurance_interest_percentage)

        self.total = self.income_tax_accumulate() + self.income_invest_accumulate()
        # output - input / year / input
        self.times = (self.total + self.final_return_money) / (self.payment_amout * self.payment_year)
        self.interest_per_year = ((self.total + self.final_return_money) - (self.payment_amout * self.payment_year)) \
                                    / self.coverage_year / (self.payment_amout * self.payment_year) * 100


    def __str__(self):
        return f"{self.total} , {self.times} , {self.interest_per_year}, "

    def percentage(self, money_amount , percentage):
        return money_amount * percentage / 100

    def income_tax_accumulate(self):
        total_investment_money = 0
        for year in range(self.coverage_year , self.coverage_year - self.payment_year , -1):
            total_investment_money += self.reinvestment(self.return_money_from_tax,
                                                self.reinvestment_interest_percentage,
                                                year, 1)
        return total_investment_money

    def income_invest_accumulate(self):
        total_investment_money = 0
        for year in range(self.coverage_year - 1 , 0 , -1):
            total_investment_money += self.reinvestment(self.return_money_from_insurance,
                                                self.reinvestment_interest_percentage,
                                                year, 1)
        return total_investment_money

    def reinvestment(self, money_amout, interest, year, compounded):
        return money_amout * (1 + interest / 100 / compounded) ** (year * compounded)


def main():
    tax = Tax()
    print(tax)

if __name__ == "__main__":
    main()
