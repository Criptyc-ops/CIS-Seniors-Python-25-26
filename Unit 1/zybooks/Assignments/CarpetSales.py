'''
program: CarpetSales.py
author: Jonathan Robinson
Date: 10/16/2025
course: CIS 25-26

Step 1: Read from input the carpet price per square foot (float), room width (int) and room length (int). Calculate the room area in square feet. Calculate the carpet price based on square feet with an additional 20% for waste. Output square feet and carpet cost. Submit for grading to confirm 1 test passes.
'''

# initialize constants
TAX_RATE = 0.07
WASTE_PCT = 1.20
LABOR_RATE = 0.75

totalsales = 0

# Order #1
# Input price per sq foot, room width and room length
price = float(input("Enter price per square foot:"))
width = int(input("Enter the width of the room: "))
length = int(input("Enter the length of the room: "))

#calculate room square feet
sq_ft = width * length

#calculate carpet cost including 20% waste
carpet = (sq_ft * WASTE_PCT) * price

#calculate labor cost (.75 per sq ft)
labor = sq_ft * LABOR_RATE

#calculate sales tax (7%)
tax = (carpet + labor) * TAX_RATE

#calculate total cost
cost= carpet + labor + tax

#output results
print("Order #1")
print(f"Square feet: {sq_ft}")
print(f"Carpet: ${carpet:,.2f} sq ft")
print(f"Labor: ${labor:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Cost: ${cost:,.2f}")
print("\n")
totalsales += cost

# Order #2
print("\nFor order 2, add the price per sq ft, width, and length all separated by a space. Ex. 2.45 16 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)

#calculations
sq_ft = width * length
carpet = (sq_ft * WASTE_PCT) * price
labor = sq_ft * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
cost = carpet + labor + tax

print("Order #2")
print(f"Square feet: {sq_ft}")
print(f"Carpet: ${carpet:,.2f} sq ft")
print(f"Labor: ${labor:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Cost: ${cost:,.2f}")
print("\n")
totalsales += cost

# Order #3
print("For order 3, add the price per sq ft, width, and length all separated by a space. Ex. 2.45 16 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)

#calculations
sq_ft = width * length
carpet = (sq_ft * WASTE_PCT) * price
labor = sq_ft * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
cost = carpet + labor + tax

print("Order #3")
print(f"Square feet: {sq_ft}")
print(f"Carpet: ${carpet:,.2f} sq ft")
print(f"Labor: ${labor:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Cost: ${cost:,.2f}")
print("\n")
totalsales += cost

#output total sales
print(f"Total sales: ${totalsales:,.2f}")