'''
python has a module named random that provides functions that generate random numbers
to use the random module, you must first import it
'''
import random
for roll in range (45667654):
    print(random.randint(1,2), end=' ')


    # Second example
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    mynumber = random.randint(smaller, larger)
    count = 0
    guess = -1
    while True:
        count += 1
        userNumber = int(input("Enter your guess: "))
        if userNumber < mynumber:
            print("too small!")
        elif userNumber > mynumber:
            print("too large!")
        else:
            print("you got it in", count, "tries")
            break