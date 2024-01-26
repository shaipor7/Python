def income_invest_accumulate(investments):
    total_investment_money = 0
    for i in range(len(investments)):
        total_investment_money = reinvestment(investments[i]["start"],
                                        investments[i]["return_rate"],
                                        investments[i]["after"], investments[i]["compound"])
        try:
            investments[i+1]["start"] = total_investment_money
        except:
            pass
    return round(total_investment_money,2)

def addition(investments):
    investments_dca = investments
    total_monthly = 0
    reinvest_dca = 0
    for i in range(len(investments)):
        print(investments)
        # Assign the values
        total_year = investments[i]["after"]
        total_months = total_year * investments[i]["contribute"]
        compound_frequency = investments[i]["compound"]
        annual_interest_rate = investments[i]["return_rate"]
        monthly_deposit = investments[i]["addition"]

        # Calculate the future value for each monthly deposit
        for month in range(1, total_months):
            # Time left until the end of the 10 years (in years)
            time_left = (total_months - month) / investments[i]["contribute"]

            # Number of times interest applied to this particular deposit
            compound_times = compound_frequency * time_left

            # Future value of this particular depositm
            future_value = monthly_deposit * ((1 + annual_interest_rate / 100 / compound_frequency) ** compound_times)

            # Add the future value of this deposit to the total amount
            total_monthly += future_value
        del investments_dca[i]
        print(investments_dca)
        if len(investments_dca) > 0:
            investments_dca[i]["start"] = total_monthly
            print(total_monthly)
            reinvest_dca += income_invest_accumulate(investments_dca)
            print(total_monthly)
    if monthly_deposit > 0:
        total_monthly += monthly_deposit

    return round(total_monthly,2)

# Compounded interest formula
def reinvestment(money_amout, interest, year, compounded):
    return money_amout * (1 + interest / 100 / compounded) ** (year * compounded)

def main():
    Input = collect_investment_data()
    print(Input)
    print(income_invest_accumulate(Input))
    print(addition(Input))
    print(f"{income_invest_accumulate(Input)+addition(Input):,}")

# Get user input as a list of dict
def collect_investment_data():
    investments = []
    investment_data = {}
    investment_data['start'] = get_input("Starting Amount ($): ", int)
    while True:
        investment_data['after'] = get_input("After (years): ", int)
        investment_data['return_rate'] = get_input("Return rate (%): ", float)
        investment_data['compound'] = get_compound("Compound (Annually, Semiannually, Quarterly, Monthly): ")
        investment_data['addition'] = get_input("Additional Contribution ($): ", int)
        investment_data['contribute'] = get_contribute("Contributed each (Month or Year): ")

        investments.append(investment_data)
        continued = input("Additional investment? (yes/no): ").casefold()
        if continued in ["yes", "y"]:
            investment_data = {}
            pass
        else:
            break
    return investments

# Check the input type and re-prompt the user if it's not
def get_input(message, input_type):
    while True:
        try:
            return input_type(input(message))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

# Check the input type and re-prompt the user if it's not, then then convert to numbers
def get_compound(message):
    while True:
        try:
            Input = input(message).strip().casefold()
            if Input == "a" or Input == "annually":
                return 1
            elif Input == "s" or Input == "semiannually":
                return 2
            elif Input == "q" or Input == "quarterly":
                return 4
            elif Input == "m" or Input == "monthly":
                return 12
            else : raise ValueError
        except ValueError:
            print("Invalid input")

# Check the input type and re-prompt the user if it's not, then convert to numbers
def get_contribute(message):
    while True:
        try:
            Input = input(message).strip().casefold()
            if Input == "m" or Input == "month":
                return 12
            elif Input == "y" or Input == "year":
                return 1
            else : raise ValueError
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()
