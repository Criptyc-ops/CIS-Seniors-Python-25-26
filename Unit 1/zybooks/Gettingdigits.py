'''
given a number, % and // can be used to get each digit. For the three-digit number user_val like 927
'''

mydigit = int(input("Enter a three-digit number: "))

ones_digit = mydigit % 10
tmp_val = mydigit // 10

tens_digit = tmp_val % 10
tmp_val = tmp_val // 10

hundreds_digit = tmp_val % 10

print("the ones place is", ones_digit, ", the tens place is", tens_digit, ", and the hundreds place is", hundreds_digit)