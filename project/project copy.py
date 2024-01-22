class Tax():
    def __init__(self):
        self.start = int(input("Starting Amount ($): "))
        self.after = int(input("After (years): "))
        self.return_rate = int(input("Return rate (%): "))
        self.compound = input("Compound (Annually ,Semiannually, Quarterly, Monthly): ")
        self.addition = int(input("Additional Contribution ($): "))
        self.
        Additional Contribution
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
