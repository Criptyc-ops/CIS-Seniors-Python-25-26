'''
program: whileLoop.py
author: Jonathan Robinson
date: 10-02-2025
course: CIS 25-26
set the sum to 0.0
input a string
while the string is not the empty string
    convert the string to a float
    add the float to the sum
    input a string
print the sum

loop Control variable - The first input statement that initializes the variable to a value that the loop condition can test.
'''

theSum = 0.0
data = input("Enter a number or press Enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or press Enter to quit: ")
print("The sum is: ", theSum)

print("\n\nA count-controlled while loop")

# Summation with a for loop
theSum = 0.0
count = 1
while count <= 10000:
    theSum += count
    count += 1 # Ctontrol variable needs to increment
    print(theSum)

#Counting down with a for Loop
for count in range(10, 0, -1):
    print(count, end=' ')

#Counting down with a while loop
count = 10
while count > 1:
    print(count, end=' ')
    count -= 1

theSum = 0.0
while True:
    data = input("\nEnter a number or press Enter to quit: ")
    if data == "": #Termination condition
        break       # the break statement will end the loop
    number = float(data)
    theSum += number
print("The sum is: ", theSum)

while True:
    number = int(input("Enter a numeric grade: "))
    if number <= 0 and number >= 100:
        break
    else: print("Invalid grade, try again, must be between 0 and 100")
print(number) #echo the valid input

done = False
while not done:  # While not == false
    number = int(input("Enter a numeric grade: "))
    if number <= 0 and number >= 100:
        done = True
    else: print("Invalid grade, try again, must be between 0 and 100")
print(number) #echo the valid input



