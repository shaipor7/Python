# Investment Calculator

#### Video Demo:  <URL HERE>
## Description:
This Python script calculates the future value of investments based on various parameters, including starting amount, return rate, compounding frequency, additional contributions, and contribution frequency. The script provides two methods for calculating the total investment: one based on a single initial investment and another based on Dollar-Cost Averaging (DCA).

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

3. View the calculated results, including a tabulated summary of investments, total investments from the starting money, total investments from DCA, and overall total investments.

### Input Details
Starting Amount: Initial amount of money invested.
After (Years): Duration of the investment in years.
Return Rate (%): Annual return rate on the investment.
Compound: Compounding frequency (Annually, Semiannually, Quarterly, Monthly).
Additional Contribution ($): Additional money contributed regularly.
Contributed Each (Month or Year): Frequency of additional contributions (Monthly or Yearly).
