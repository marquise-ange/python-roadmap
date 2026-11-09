
import numpy as np

# 1. Create students and courses
students = ["Alice", "Brian", "Clara", "David", "Esther"]

courses = ("Python", "Database", "Big Data")

# 2. Create a dictionary to store student marks
student_marks = {}

# 3. Enter marks for each student
for student in students:
    print(f"\nEnter marks for {student}:")

    marks = []

    for course in courses:
        mark =float(input(f"\ Enter {course} marks"))
        while marks < 0 or mark > 100:
            print ("Invalid marks!, Enter a value between 0 and 100")
            mark =float(input(f"\ Enter  a valid {course} marks for {student}"))
            marks.append(marks)
            student_marks[student] = marks

        



