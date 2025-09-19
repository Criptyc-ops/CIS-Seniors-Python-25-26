'''
Filename: input.py
Name: Jonathan Robinson
course: CIS 25-26
Date: 2025-09-19
'''

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = input("How old are you? ")
math = input("what is pi? ")
favorite = input("What is your favorite class? ")



print("Hello, " + first_name + " " + last_name + "!")
print("You are " + age + " years old.")
print("You said pi is " + math + ".")
print("Your favorite class is " + favorite + ".")

if favorite == "yes":
    favorite = "CIS"
    print("I am happy to hear this is your favorite class!")
else:
    favorite = "false"
    print("NO! That is NOT solid snake!")