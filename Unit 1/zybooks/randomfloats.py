#import random module
import random

#generate random float between 0 and 1
print(random.random())
print(random.random())
print(random.random())

#using randrange()
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))

print()
print("using a seed.")
random.seed(15) # Generate same sequence of random intergers between 1 and 10
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))