'''
filename: quizScorer.py
author: Jonathan Robinson
date: 2025-09-25
course: CIS 25-26
'''
print("Quiz Scorer")
#inputs
name = input("what is your students name? ")
test = input("how many questions were on the quiz? ")

print ("\nHello", name, "you had", test, "questions on your quiz.")
print("\n")

print("These are the students answers! (1 for correct, 0 for incorrect)")
totalCorrect = 0  # initialize before the loop
for question in range(int(test)):
    answer = int(input("Question " + str(question + 1) + ": "))
    if answer == 1:
        print("Correct")
        totalCorrect += 1
    elif answer == 0:
        print("Incorrect")
    else:
        print("Invalid input, please enter 1 or 0")

# After the loop, calculate and display the score
score = (totalCorrect / int(test)) * 100
print("\n", name, "you got", totalCorrect, "out of", test, "questions correct.")
print("Your score is:", float(score), "%")
if score >= 70:
    print("You passed!")
else:
    print("You did not pass.")