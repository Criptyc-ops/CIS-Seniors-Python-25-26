'''
file: quizTracker.py
author: Jonathan Robinson
date: 2025-10-01
course: CIS 25-26
'''

print("="*40)
print("Welcome to the Grade Tracker Program!")
print("="*40)

# Get number of students
while True:
    student_count = input("Enter number of students to track (1-20): ")
    if student_count.isdigit():
        student_count = int(student_count)
        if student_count >= 1 and student_count <= 20:
            break
        else:
            print("Please enter a number between 1 and 20.")
    else:
        print("Invalid input. Please enter a valid number.")

# Initialize variables
students = []
total_points = 0
highest_score = None
lowest_score = None
pass_count = 0
grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0
grade_F = 0

# Collect student data
for i in range(student_count):
    print("\n--- Student " + str(i+1) + " ---")
    name = input("Enter student name: ").strip()
    while True:
        score_input = input("Enter test score (0-100): ")
        try:
            score = float(score_input)
            if score >= 0 and score <= 100:
                break
            else:
                print("Please enter a number between 0 and 100.")
        except:
            print("Invalid input. Please enter a valid number.")

    # Assign letter grade
    if score >= 90:
        letter = 'A'
        grade_A += 1
    elif score >= 80:
        letter = 'B'
        grade_B += 1
    elif score >= 70:
        letter = 'C'
        grade_C += 1
    elif score >= 60:
        letter = 'D'
        grade_D += 1
    else:
        letter = 'F'
        grade_F += 1

    students.append([name, score, letter])

    total_points += score
    if highest_score is None or score > highest_score:
        highest_score = score
    if lowest_score is None or score < lowest_score:
        lowest_score = score
    if score >= 70:
        pass_count += 1

average_score = total_points / student_count

# Find students above/below average
above_avg = []
below_avg = []
for i in range(student_count):
    if students[i][1] > average_score:
        above_avg.append(students[i][0])
    elif students[i][1] < average_score:
        below_avg.append(students[i][0])

print("\n" + "="*40)
print("Grade Tracker Results")
print("="*40)
print("Total students:", student_count)
print("Total points earned: %.2f" % total_points)
print("Average class score: %.2f" % average_score)
print("Highest score: %.2f" % highest_score)
print("Lowest score: %.2f" % lowest_score)
print("Number of students who passed (≥70):", pass_count)
print("\nGrade Distribution:")
print("  A:", grade_A)
print("  B:", grade_B)
print("  C:", grade_C)
print("  D:", grade_D)
print("  F:", grade_F)

print("\nStudents above average:")
if len(above_avg) > 0:
    print("  " + ", ".join(above_avg))
else:
    print("  None")
print("Students below average:")
if len(below_avg) > 0:
    print("  " + ", ".join(below_avg))
else:
    print("  None")

print("\nDetailed Student Grades:")
print("-"*40)
for i in range(student_count):
    print(students[i][0] + ": %.2f" % students[i][1] + " (" + students[i][2] + ")")
print("="*40)