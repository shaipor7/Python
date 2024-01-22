class Tax():
    def __init__(self):
        self.start = self.get_input("Starting Amount ($): ", int)
        self.after = self.get_input("After (years): ", int)
        self.return_rate = self.get_input("Return rate (%): ", float)
        self.compound = self.get_compound("Compound (Annually, Semiannually, Quarterly, Monthly): ")
        self.addition = self.get_input("Additional Contribution ($): ", int)
        self.contribute = self.get_validated_input("Contributed each (Month or Year): ", ["Month", "Year"])

    def get_input(self, message, input_type):
        while True:
            try:
                return input_type(input(message))
            except ValueError:
                print(f"Invalid input. Please enter a valid {input_type.__name__}.")

    def get_compound(self, message):
        while True:
            user_input = input(message)
            message = user_input.strip().casefold()
            if compound == "a" or compound == "annually":
                return 1
            elif compound == "s" or compound == "semiannually":
                return 2
            elif compound == "q" or compound == "quarterly":
                return 4
            elif compound == "m" or compound == "monthly":
                return 12
            else : print("Invalid input")

    def __str__(self):
        return f"{self.total} , {self.times} , {self.interest_per_year}, "

    def Compound(self, compound):
        compound = compound.strip().casefold()
        if compound == "a" or compound == "annually":
            return 1
        elif compound == "s" or compound == "semiannually":
            return 2
        elif compound == "s" or compound == "quarterly":
            return 4
        elif compound == "s" or compound == "monthly":
            return 12
        else : raise ValueError


    def percentage(self, money_amount , percentage):
        return money_amount * percentage / 100

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
