#Task 1 — Data Parsing & Profile Cleaning

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

formated_clean_students = []

# Loop through raw data to clean and format each student's profile
for student in raw_students:
    #Format to Title Case
    formated_students_name = student['name'].strip().title()
    #Convert to Integer
    formated_students_roll = int(student['roll'])
    #Split Marks
    formated_students_marks_list = [
        int(mark) for mark in student["marks_str"].split(", ")]
    #Store and ORganise Data
    cleaned_students = {
    "name": formated_students_name,
    "roll": formated_students_roll,
    "marks": formated_students_marks_list
    }

    formated_clean_students.append(cleaned_students)
    #Validation Loop
    valid_name = True
    for word in formated_students_name.split():
        if not word.isalpha():
            valid_name= False
            break
    if valid_name:
        print(f"{formated_students_name} : ✓ Valid name")
    else:
        print(f"{formated_students_name} : ✗ Invalid name")

#Print Profile  Card          
for student in formated_clean_students:
    name = student["name"]
    roll = student["roll"]
    marks = student["marks"]

    student_card = f"""
        =======================    
        Name : {name}
        Roll : {roll}
        Marks: {marks}
        =======================
        """
    print(student_card)

#Check Roll number 103
for student in formated_clean_students:
    name = student["name"]
    roll = student["roll"]

    if roll == 103:
        print(name.lower())
    else:
        print(name.upper())

print("================================")

#Task 2 — Marks Analysis Using Loops & Conditionals

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("Student :", student_name)

print("================================")

# Determine grade based on the mark
for grades in range(len(subjects)):
    sub = subjects[grades]
    mark = marks[grades]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{sub:12} = {mark:3} | {grade}")

print("================================")
# calculate total marks
total = sum(marks)
print("Total marks  :", total)
print("================================")

# Calculate Average marks
avg = round(total / len(marks), 2)
print("Average marks:", avg)
print("================================")

high_score = marks.index(max(marks))
highest_sub = subjects[high_score]
highest_mark = marks[high_score]
print("Highest Scoring Subject :", f"{highest_sub} ({highest_mark})")
print("================================")

low_score = marks.index(min(marks))
lowest_sub = subjects[low_score]
lowest_mark = marks[low_score]
print("Lowest Scoring Subject :", f"{lowest_sub} ({lowest_mark})")
print("================================")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

new_subjects_added = 0

while True:
    sub = input("Enter subject name (type 'done' to stop): ").strip()
    if sub.lower() == "done":
        break

    mark_str = input("Enter marks (0-100): ").strip()

    try:
        mark = int(mark_str)
    except ValueError:
        print("Warning: Invalid input. Please enter a number.")
        continue

    if mark < 0 or mark > 100:
        print("Warning: Marks must be between 0 and 100.")
        continue

    subjects.append(sub)
    marks.append(mark)
    new_subjects_added += 1

updated_avg = sum(marks) / len(marks)

print(f"New subjects added : {new_subjects_added}")
print(f"Updated average    : {updated_avg:.2f}")

#Task 3 — Class Performance Summary

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

student_averages = []

print("Name            | Average | Status")
print("----------------------------------------")

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    status = "Pass" if avg >= 60 else "Fail"
    print(f"{name:15} | {avg:7.2f} | {status}")
    student_averages.append(avg)

passed = 0
failed = 0
for avg in student_averages:
    if avg >= 60:
        passed += 1
    else:
        failed += 1

topper = student_averages.index(max(student_averages))
topper_name = class_data[topper][0]
topper_avg = student_averages[topper]

class_avg = round(sum(student_averages) / len(student_averages), 2)
print("----------------------------------------")
print(f"Passed  : {passed}")
print(f"Failed  : {failed}")
print(f"Class Topper  : {topper_name} ({topper_avg:.2f})")
print(f"Class average: {class_avg:.2f}")

#Task 4 — String Manipulation Utility

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print("1. clean_essay:")
print(repr(clean_essay))
print("----------------------------------------")

title_essay = clean_essay.title()
print("2. Title Case:")
print(title_essay)
print("----------------------------------------")

count_python = clean_essay.count("python")
print("3. Count of 'python':")
print(count_python)
print("----------------------------------------")

replaced_essay = clean_essay.replace("python", "Python 🐍")
print("4. After replace:")
print(replaced_essay)
print("----------------------------------------")

sentences = clean_essay.split(". ")
print("5. Split into sentences:")
print(sentences)
print("----------------------------------------")

print("6. Numbered sentences:")
for i, s in enumerate(sentences, 1):
    if s.endswith("."):
        print(f"{i}. {s}")
    else:
        print(f"{i}. {s}.")