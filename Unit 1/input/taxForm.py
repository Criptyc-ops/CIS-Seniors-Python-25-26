'''
filename: taxForm.py
name: Jonathan Robinson
course: CIS 25-26
date: 2025-09-22
'''
print("\n\nMyTax Rate Calcuator.")
print("=" * 40)
#initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

#request the inputs
grossIncome = float(input("Enter your gross income: "))
numDependents = int(input("Enter the number of dependents: "))

#calculate the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

#display the income tax
print("The income tax is $" + str(incomeTax))