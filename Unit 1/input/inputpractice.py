'''
filename: inputpractice.py
name: Jonathan Robinson
course: CIS 25-26
date: 2025-09-19
'''

'''
first name
last name
age
favorite color
first number
second number
Favorite Tv show
Favorite movie
Favorite song
Favorite food

- Write out a paragraph outlining user data using variables. Using the First and second numbers, create 3 seperate math equations and print the values.
'''

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
favorite_tv_show = input("Enter your favorite TV show: ")
favorite_movie = input("Enter your favorite movie: ")
favorite_song = input("Enter your favorite song: ")
favorite_food = input("Enter your favorite food: ")

print("\n--- User Information ---")
# Print user information
print("Hi, my name is" + first_name + " " + last_name + ". " + "I am " + age + " years old. " + "I really like the color " + favorite_color + ". " + "My favorite TV show is " + favorite_tv_show + ", " + "my favorite movie is " + favorite_movie + ", " + "my favorite song is " + favorite_song + ", " + "and my favorite food is", favorite_food + ". " + "Thank you so much for listening to my information!")

print("\n--- Math Equations ---")
# Perform and print math equations
sum_result = first_number + second_number
print("The sum of", first_number, "and", second_number, "is:", sum_result) 
difference_result = first_number - second_number
print("The difference when you subtract", second_number, "from", first_number, "is:", difference_result) 
product_result = first_number * second_number
print("The product of", first_number, "and", second_number, "is:", product_result)






