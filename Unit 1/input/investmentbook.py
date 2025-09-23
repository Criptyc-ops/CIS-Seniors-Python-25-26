'''
Program: Investmentbook.py
Author: Jonathan Robinson
Date: 2025-09-23
Course: CIS 25-26
Compute an investment report
'''
print("\n\n")
print("=" * 60)
print("\n\n My Investment Tracker")
print("=" * 60)
#accept the Inputs
startingBalance = float(input("Enter the starting balance amount: "))
rate = int(input("Enter the annual interest rate: "))
Years = int(input("Enter the number of years to invest: "))

#Convert the rate to a decimal number
rate = rate / 100

#initialize the accumulator for the interest

#display the header for the table
print("\n\nInvestment Report")
print("=" * 60)
print("Year Starting Balance Interest Earned Ending Balance")
print("-" * 60)

#display the totals for the 