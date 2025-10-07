# Python Variable Name Validator
# Student Name: _______________
# Date: _______________

# List of Python keywords
python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]

# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()

# Get user input
variable_name = input("Enter a variable name to validate: ")

if variable_name == python_keywords:
    print("invalid variable name! That is a python keyword")
elif variable_name == (" "):
    print("invalid variable name! It cannot be a blank space")
elif variable_name.isdigit == True:
    print("invalid variable name! It cannot start with a number")


# Your validation code goes here
# Check each rule and provide appropriate feedback