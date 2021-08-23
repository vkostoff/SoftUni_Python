students = int(input())
grade_two = 0
grade_three = 0
grade_four = 0
grade_five = 0
total_grade = 0
for students in range(1, students + 1):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        grade_two += 1
        total_grade += grade
    if 3.00 <= grade <= 3.99:
        grade_three += 1
        total_grade += grade
    if 4.00 <= grade <= 4.99:
        grade_four += 1
        total_grade += grade
    if grade >= 5.00:
        grade_five += 1
        total_grade += grade

grade_two_percentage = grade_two / students * 100
grade_three_percentage = grade_three / students * 100
grade_four_percentage = grade_four / students * 100
grade_five_percentage = grade_five / students * 100
average_grade = total_grade / students

print(f"Top students: {grade_five_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {grade_four_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {grade_three_percentage:.2f}%")
print(f"Fail: {grade_two_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
