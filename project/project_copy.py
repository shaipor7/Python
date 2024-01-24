class Information():
    def __init__(self):
        self.investments = []
        self.collect_investment_data()

    def __str__(self):
        return str(self.investments)

    def collect_investment_data(self):
        investment_data = {}
        investment_data['start'] = self.get_input("Starting Amount ($): ", int)
        while True:
            investment_data['after'] = self.get_input("After (years): ", int)
            investment_data['return_rate'] = self.get_input("Return rate (%): ", float)
            investment_data['compound'] = self.get_compound("Compound (Annually, Semiannually, Quarterly, Monthly): ")
            investment_data['addition'] = self.get_input("Additional Contribution ($): ", int)
            investment_data['contribute'] = self.get_contribute("Contributed each (Month or Year): ")

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

    def get_contribute(self, message):
        while True:
            Input = input(message).strip().casefold()
            if Input == "m" or Input == "month":
                return 12
            elif Input == "y" or Input == "year":
                return 1
            else : print("Invalid input")

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

    def addition(self):
        self.total_monthly = 0
        total_months = self.investments[0]["after"] * self.investments[0]["contribute"]
        compound_frequency = self.investments[0]["compound"]
        annual_interest_rate = self.investments[0]["return_rate"] / 100
        monthly_deposit = self.investments[0]["addition"]
        # Calculate the future value for each monthly deposit
        for month in range(1, total_months):
            # Time left until the end of the 10 years (in years)
            time_left = (total_months - month ) / self.investments[0]["contribute"]

            # Number of times interest applied to this particular deposit
            compound_times = compound_frequency * time_left

            # Future value of this particular deposit
            future_value = monthly_deposit * ((1 + annual_interest_rate / compound_frequency) ** compound_times)

            # Add the future value of this deposit to the total amount
            self.total_monthly += future_value

        self.total_monthly += self.investments[0]["start"]

        return self.total_monthly

    def reinvestment(self, money_amout, interest, year, compounded):
        return money_amout * (1 + interest / 100 / compounded) ** (year * compounded)



def main():
    Input = Information()
    Invest = Investment(Input.investments)
    print(Invest.income_invest_accumulate() +Invest.addition())

def collect_investment_data():
    investment_data = {}
    investment_data['start'] = self.get_input("Starting Amount ($): ", int)
    while True:
        investment_data['after'] = self.get_input("After (years): ", int)
        investment_data['return_rate'] = self.get_input("Return rate (%): ", float)
        investment_data['compound'] = self.get_compound("Compound (Annually, Semiannually, Quarterly, Monthly): ")
        investment_data['addition'] = self.get_input("Additional Contribution ($): ", int)
        investment_data['contribute'] = self.get_contribute("Contributed each (Month or Year): ")

        self.investments.append(investment_data)
        continued = input("Additional investment? (yes/no): ").casefold()
        if continued in ["yes", "y"]:
            investment_data = {}
            pass
        else:
            break
    return
if __name__ == "__main__":
    main()
