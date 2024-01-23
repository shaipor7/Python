class Information:
    def __init__(self):
        self.investments = []
        self.collect_investment_data()

    def collect_investment_data(self):
        while True:
            investment_data = {
                'start': self.get_input("Starting Amount ($): ", int),
                'after': self.get_input("After (years): ", int),
                'return_rate': self.get_input("Return rate (%): ", float),
                'compound': self.get_compound("Compound (Annually, Semiannually, Quarterly, Monthly): "),
                # 'addition':  self.get_input("Additional Contribution ($): ", int),
                # 'contribute': self.get_contribute("Contributed each (Month or Year): "),
            }

            self.investments.append(investment_data)

            if input("Additional investment? (yes/no): ").casefold() not in ["yes", "y"]:
                break

    def get_input(self, message, input_type):
        while True:
            try:
                return input_type(input(message))
            except ValueError:
                print(f"Invalid input. Please enter a valid {input_type.__name__}.")

    def get_compound(self, message):
        compound_options = {'a': 1, 'annually': 1, 's': 2, 'semiannually': 2,
                            'q': 4, 'quarterly': 4, 'm': 12, 'monthly': 12}
        while True:
            user_input = input(message).casefold()
            if user_input in compound_options:
                return compound_options[user_input]
            else:
                print("Invalid input")

    # def get_contribute(self, message):
    #     while True:
    #         Input = input(message).strip().casefold()
    #         if Input == "m" or Input == "month":
    #             return 12
    #         elif Input == "y" or Input == "year":
    #             return 1
    #         else : print("Invalid input")


class Investment:
    def __init__(self, investments):
        self.investments = investments
        self.total_investment_money = self.calculate_total_investment()

    def calculate_total_investment(self):
        total_investment = 0
        for investment in self.investments:
            total_investment = self.reinvestment(investment["start"],
                                                 investment["return_rate"],
                                                 investment["after"],
                                                 investment["compound"])
        return total_investment

    def reinvestment(self, amount, interest, years, compounded):
        return amount * (1 + interest / 100 / compounded) ** (years * compounded)


def main():
    user_inputs = Information()
    investment = Investment(user_inputs.investments)
    print(f"Total Investment Money: {investment.total_investment_money}")

if __name__ == "__main__":
    main()
