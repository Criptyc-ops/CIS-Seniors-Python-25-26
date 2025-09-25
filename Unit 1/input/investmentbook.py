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
totalInterest = 0.0
#display the header for the table
print("\n\nInvestment Report")
print("=" * 60)
print("%4s%18s%10s%16s" % ("Year", "Starting Balance", " Interest Earned", "Ending Balance"))
print("-" * 60)

#display the totals for each year
for year in range(1, Years + 1):
    interest = startingBalance * rate
    endBalance = startingBalance + interest
    totalInterest += interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startingBalance, interest, endBalance))
    startingBalance = endBalance

#display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)
