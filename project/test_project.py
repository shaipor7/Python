monthly_deposit = 1000  # Monthly deposit
annual_interest_rate = 0.10  # Annual interest rate (10%)
compound_frequency = 4  # Quarterly compounding
total_months = 10 * 12  # Total months in 10 years
total_amount = 0  # Initialize total amount

# Calculate the future value for each monthly deposit
for month in range(1, total_months + 1):
    # Time left until the end of the 10 years (in years)
    time_left = (total_months - month + 1) / 12

    # Number of times interest applied to this particular deposit
    compound_times = compound_frequency * time_left

    # Future value of this particular deposit
    future_value = monthly_deposit * ((1 + annual_interest_rate / compound_frequency) ** compound_times)

    # Add the future value of this deposit to the total amount
    total_amount += future_value

total_amount
