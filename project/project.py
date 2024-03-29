from tabulate import tabulate

# Function to calculate starting amount of money
def starting_term(investments):
    total_investment_money = 0
    for i in range(len(investments)):
        total_investment_money = reinvestment(investments[i]["start"],
                                        investments[i]["return_rate"],
                                        investments[i]["after"], investments[i]["compound"])
        # Continue invest for more terms
        try:
            investments[i+1]["start"] = total_investment_money
        except:
            pass
    return round(total_investment_money,2)

# Function to calculate DCA
def dca_term(investments):

    # Assign the values
    investments_dca = investments.copy()
    reinvest_dca = 0
    for i in range(len(investments)):
        monthly = 0
        total_year = investments[i]["after"]
        total_months = total_year * investments[i]["contribute"]
        compound_frequency = investments[i]["compound"]
        annual_interest_rate = investments[i]["return_rate"]
        monthly_deposit = investments[i]["addition"]

        # Calculate the future value for each monthly deposit
        for month in range(1, total_months):
            # Time left until the end of the X years
            time_left = (total_months - month) / investments[i]["contribute"]
            # Conver to number of times interest
            compound_times = compound_frequency * time_left
            # Future value of this particular deposit
            future_value = monthly_deposit * ((1 + annual_interest_rate / 100 / compound_frequency) ** compound_times)
            # Add the future value to the total amount
            monthly += future_value

        # Check the final amount which is not calculated
        if monthly_deposit > 0:
            monthly += monthly_deposit

        # Calculate reinvest for each DCA term
        del investments_dca[0]

        if len(investments_dca) > 0:
            investments_dca[0]["start"] = monthly
            reinvest_dca += starting_term(investments_dca)

    return round(monthly + reinvest_dca,2)

def total_contribute(investments):
    total = 0
    for i in range(len(investments)):
        total += investments[i]['contribute'] * investments[i]['addition']
    return total

# Compounded interest formula
def reinvestment(money_amout, interest, year, compounded):
    return money_amout * (1 + interest / 100 / compounded) ** (year * compounded)

def main():
    Input = collect_investment_data()
    # Prepare data for tabulation
    headers = ["Start", "After (Years)", "Return Rate (%)", "Compound", "Addition", "Contribute"]
    rows = [[inv.get('start', 'N/A'), inv.get('after'), inv.get('return_rate'), inv.get('compound'), inv.get('addition'), inv.get('contribute')] for inv in Input]

    # Create a tabulated string
    table = tabulate(rows, headers=headers, tablefmt="grid")

    # Print the table
    print(table)
    print(f"Total contribute money: ${total_contribute(Input)}")
    print(f"Total investments from starting money: ${starting_term(Input):,}")
    print(f"Total investments from DCA: ${dca_term(Input):,}")
    print(f"End Balance: ${starting_term(Input)+dca_term(Input):,.2f}")


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
        if investment_data['addition'] != 0:
            investment_data['contribute'] = get_contribute("Contributed each (Month or Year): ")
        else: investment_data['contribute'] = 0
        investments.append(investment_data)
        continued = input("Continued investment? (yes/no): ").casefold()
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
