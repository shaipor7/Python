class Information():
    def __init__(self):
        self.investments = []
        self.collect_investment_data()

    def collect_investment_data(self):
        investment_data = {}
        investment_data['start'] = self.get_input("Starting Amount ($): ", int)
        while True:
            investment_data['after'] = self.get_input("After (years): ", int)
            investment_data['return_rate'] = self.get_input("Return rate (%): ", float)
            investment_data['compound'] = self.get_compound("Compound (Annually, Semiannually, Quarterly, Monthly): ")
            # investment_data['addition'] = self.get_input("Additional Contribution ($): ", int)
            # investment_data['contribute'] = self.get_contribute("Contributed each (Month or Year): ")

            self.investments.append(investment_data)
            continued = input("Additional investment? (yes/no): ").casefold()
            if continued in ["yes", "y"]:
                investment_data = {}
                pass
            else:
                break

    def get_input(self, message, input_type):
        while True:
            try:
                return input_type(input(message))
            except ValueError:
                print(f"Invalid input. Please enter a valid {input_type.__name__}.")

    def get_compound(self, message):
        while True:
            Input = input(message).strip().casefold()
            if Input == "a" or Input == "annually":
                return 1
            elif Input == "s" or Input == "semiannually":
                return 2
            elif Input == "q" or Input == "quarterly":
                return 4
            elif Input == "m" or Input == "monthly":
                return 12
            else : print("Invalid input")

    # def get_contribute(self, message):
    #     while True:
    #         Input = input(message).strip().casefold()
    #         if Input == "m" or Input == "month":
    #             return 12
    #         elif Input == "y" or Input == "year":
    #             return 1
    #         else : print("Invalid input")

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

class Investment():
    def __init__(self, investments):
        self.investments = investments
        self.income_invest_accumulate()
        print(self.investments)

    # def __str__(self):
    #     return f"{self.total} , {self.times} , {self.interest_per_year}, "

    def percentage(self, money_amount , percentage):
        return money_amount * percentage / 100

    def income_invest_accumulate(self):
        self.total_investment_money = 0
        for i in range(len(self.investments)):
            self.total_investment_money = self.reinvestment(self.investments[i]["start"],
                                                self.investments[i]["return_rate"],
                                                self.investments[i]["after"], self.investments[i]["compound"])
            try:
                self.investments[i+1]["start"] = self.total_investment_money
            except:
                pass
        return self.total_investment_money

    def reinvestment(self, money_amout, interest, year, compounded):
        return money_amout * (1 + interest / 100 / compounded) ** (year * compounded)


def main():
    Input = Information()
    Invest = Investment(Input.investments)
    print(Invest.total_investment_money)

if __name__ == "__main__":
    main()
