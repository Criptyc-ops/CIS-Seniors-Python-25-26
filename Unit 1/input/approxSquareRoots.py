'''
program: approxSquareRoots.py
author: Jonathan Robinson
date: 10-02-2025
course: CIS 25-26

Request: write a program that computes square roots. You will use pytjon's math module. Python's math module has a function called sqrt = math.sqrt() - will only be used at the end to compare your caluculation with Python's calculation.

Compute the square root of a number:
1. The input is a number.
2. The outputs are the program's estimate of the square root using Newton's method of successive approximations, and Python's own estimate usong math.sqrt().
'''
import math

# Receive the input number from the user

x = float(input("Enter a number to compute the square root: "))

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

# perform the successive approximations
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

# output the results
print("The estimate of the square root is:", estimate)
print("Python's estimate of the square root is:", math.sqrt(x))