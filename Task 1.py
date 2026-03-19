# Task 1: Create a Dictionary of Student Marks

student_marks = {
    "Alice": 85,
    "Rajuuuu": 65,
    "Don": 95
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: ")
else:
    print("Student not found")
