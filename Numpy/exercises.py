import numpy as np

# Create NumPy array
marks = np.array([45, 80, 67, 92, 55, 75])

# Calculate total marks
total_marks = np.sum(marks)
print("Total marks:", total_marks)

# Calculate average marks
average = np.mean(marks)
print("Average marks:", average)

# Find minimum
minimum = np.min(marks)
print("Minimum marks:", minimum)

# Find maximum
maximum = np.max(marks)
print("Maximum marks:", maximum)

# Find marks above 70
passed = marks[marks > 70]
print("Marks above 70:", passed)


# Count students who scored above 70
count = np.sum(marks > 70)
print("Number of students above 70:", count)