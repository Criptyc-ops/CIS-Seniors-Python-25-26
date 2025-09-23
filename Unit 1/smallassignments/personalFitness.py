"""
file: personalFitness.py
name: Jonathan Robinson
date: 09-23-2025
class = CIS 25-26
"""
# User specific data
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_in_inches = float(input("Enter your height in inches: "))
weight_in_pounds = float(input("Enter your weight in pounds: "))
excerise_hours = float(input("Enter the number of hours you exercise per week: "))
fitness_goals = str(input("Enter your fitness goals: "))

# Calculations to preform
bmi = (weight_in_pounds / (height_in_inches ** 2)) * 703
bmi = round(bmi, 2)
ideal_weight = (height_in_inches - 60) * 2.3 + 110
ideal_weight = round(ideal_weight, 2)
Weekly_calories = excerise_hours * 500

# Print the results
print("\nPersonal Fitness Report")
print("-----------------------")
print("Name: " + name)
print("Age: " + str(age))
print("Height (inches): " + str(height_in_inches))
print("Weight (pounds): " + str(weight_in_pounds))  
print("Hours of exercise per week: " + str(excerise_hours))
print("Fitness Goals: " + fitness_goals)
print("Body Mass Index (BMI): " + str(bmi))
print("Ideal Weight (pounds): " + str(ideal_weight))
print("Estimated Weekly Calories Burned: " + str(Weekly_calories))

