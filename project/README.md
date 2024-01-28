# Investment Calculator

#### Video Demo:  <URL HERE>
## Why this Project Matters:
In today's dynamic financial landscape, making informed investment decisions is crucial for securing financial stability and future prosperity. Thus, having a tool that empowers you to calculate and plan your investments is invaluable.

Many investor beginner uses Dollar-Cost Averaging (DCA). DCA is a popular investment strategy that involves making regular contributions to your investment portfolio, regardless of market conditions. This disciplined approach helps mitigate the impact of market volatility and allows investors to benefit from fluctuations in asset prices over time.

In addition, DCA always come with compounded interest. Compounded interest is like a snowball effect for your money. As your investments generate returns, those returns are added to your initial investment, and the total amount continues to grow. Over time, you not only earn interest on your original investment but also on the interest that has already been added.

## About This Calculator

Many online investment calculators provide insights for a single investment period. However, the real world often involves multi-term investments with changing conditions. This Python script offers a comprehensive solution by allowing users to input multiple investment terms, considering compounding interest, additional contributions, and varying durations.

## Features

- **Single Investment Calculation:** Calculate the future value of a single investment over a specified period, considering compounding interest.

- **Dollar-Cost Averaging (DCA) Calculation:** Estimate the future value of investments made through DCA, including reinvestments over multiple terms.


## Getting Started

### Prerequisites

- Python 3.x
- [tabulate](https://pypi.org/project/tabulate/) library

### Installation

1. Clone the repository:

    ```bash
   git clone https://github.com/code50/116163643.git
2. Install required libraries:
    ```bash
    pip install tabulate
### Usage
1. Run the script:
    ```bash
    cd project/
    python project.py
2. Enter the investment details as prompted.

3. View the calculated results, including a tabulated summary of investments data input, total investments from the starting money, total investments from DCA, and overall total investments.

### Input Details
1. **Starting Amount:** Initial amount of money invested.
1. **After (Years):** Duration of the investment in years.
3. **Return Rate (%):** Annual return rate on the investment.
4. **Compound:** Compounding frequency (Annually, Semiannually, Quarterly, Monthly).
5. **Additional Contribution ($):** Additional money contributed regularly.
6. **Contributed Each (Month or Year):** Frequency of additional contributions (Monthly or Yearly).
7. **Continued Investment (yes/no):** Asking for more term of investments

### For example

<video src="example.mp4" controls title="example_video"></video>

## In Details

The project folder contains 2 scripts: the first one is `project.py, which includes the main function and other functions to calculate compounded interest, and the second one is test_project.py, which includes test functions to assert its correctness.

In the project.py file, there are several functions:

1. `collect_investment_data():`Prompts a user to input the investment data, then stores it as a list of dictionaries (or multiple dictionaries if there are many investment terms). Additionally, this function includes other functions to check the user input and transform it for calculation, such as:

    - `get_input(message, input_type):` Prompts a user with the specified message, then checks the user input type and re-prompts the user if it does not match the specified input_type. It is used to collect:
        - **Starting Amount**
        - **After (Years)**
        - **Return Rate (%)**
        - **Additional Contribution ($)**
        - **Continued Investment (yes/no)**.

    - `get_compound(message):` Prompt a user as `message`, then check the user input and re-prompt the user if it is not first letter or full-text of *Annually, Semiannually, Quarterly, Monthly*. It is used to collect **Compound**.

    - `get_contribute(message):` Prompt a user as `message`, then check the user input and re-prompt the user if it is not first letter or full-text of *Month, Year*. It is used to collect **Contributed Each (Month or Year)**.

2. `starting_term(investments):` Interpret the input data from `collect_investment_data()`, then calculate and return a compound interest form starting amount by using formula in `reinvestment(money_amout, interest, year, compounded)`.

3. `dca_term(investments):` Calculate and return a compound interest form DCA amount.

4. `total_contribute(investments):` Calculate and return total contribute amount.

