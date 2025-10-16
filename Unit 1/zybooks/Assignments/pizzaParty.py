'''
program: pizzaParty.py
author: Jonathan Robinson
Date: 10/16/25
course: CIS 25-26

Step 1: Read from input the number of people (int), average slices per person (float) and cost of one pizza (float). Calculate the number of whole pizzas needed (8 slices per pizza). There will likely be leftovers for breakfast. Hint: Use the ceil() function from the math library to round up to the nearest whole number and convert to an int. Calculate and output the cost for all pizzas. Submit for grading to confirm test 1 passes.
'''
import math
SLICES = 8
TAX_RATE = 0.07
DELIVERY = 0.20

weekend_total = 0

#friday night party
#inputs
num_people = int(input("Enter number of people: "))
avg_slices = float(input("Enter average slices per person: "))
pizza_cost = float(input("Enter cost per pizza: "))

#calulations
pizza_needed = (num_people * avg_slices) / SLICES
num_pizzas = math.ceil(pizza_needed)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_total += total_cost

#outputs
print("Friday Night Party!")
print(f"{num_pizzas} Pizzas: ${cost:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Delivery: ${delivery_fee:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
print("\n")

#saturday night party
#inputs
num_people = int(input("Enter number of people: "))
avg_slices = float(input("Enter average slices per person: "))
pizza_cost = float(input("Enter cost per pizza: "))

#calulations
pizza_needed = (num_people * avg_slices) / SLICES
num_pizzas = math.ceil(pizza_needed)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_total += total_cost

#outputs
print("Saturday Night Party!")
print(f"{num_pizzas} Pizzas: ${cost:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Delivery: ${delivery_fee:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
print("\n")


#sunday night party
#inputs
num_people = int(input("Enter number of people: "))
avg_slices = float(input("Enter average slices per person: "))
pizza_cost = float(input("Enter cost per pizza: "))

#calulations
pizza_needed = (num_people * avg_slices) / SLICES
num_pizzas = math.ceil(pizza_needed)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_total += total_cost

#outputs
print("Sunday Night Party!")
print(f"{num_pizzas} Pizzas: ${cost:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Delivery: ${delivery_fee:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
print("\n")


#weekend total
print(f"Weekend Total: ${weekend_total:,.2f}")