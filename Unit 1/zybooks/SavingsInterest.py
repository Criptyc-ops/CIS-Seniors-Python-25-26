'''
an example of using the math module to calculate the interest earned on a savings account
'''
import math

base = float(input("enter initial savings: "))
print()

rate = float(input("enter annual interest % rate: "))
print()

years= int(input("enter years that pass: "))
print()

total = base * math.pow((1 + rate / 100), years)

print (f"savings after {years} years is: ${total:,.2f}")