"""
Program: investment.py
Author: Jonathan Robinson
Date: 2025-09-22
Course: CIS 25-26


compute an investment report
1. The inputs are:
    a. the starting investment amount
    b. the annual interest rate
    c. the number of years to invest

2. The report is displayed in tabular form with a header
3. Computations and outputs:
    for each year
    compute the interest earned
    compute the ending balance
    display the year, starting balance, interest earned, and ending balance
4.The ending investment and interest you have paid in total are also displayed
"""

# Accept the inputs
startingInvestment = float(input("Enter the starting investment amount: "))
Interest_Rate = float(input("Enter the annual interest rate (in %): "))
num_Years = int(input("Enter the number of years to invest: "))

# convert the rate to a decimal number

rate = Interest_Rate / 100

# Initialize the accumulator for the intestest
accumulated_Interest = 0.0


#display the header for the table
print("\n\nInvestment Report")
print("=" * 60)
print("Year Starting Balance Interest Earned Ending Balance")
print("-" * 60)

#computer and display the results for each year

