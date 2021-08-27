name = input()
sum_grades = 0
grade = 1
expelled = 0
while grade <= 12:
    current_grade = float(input())
    if current_grade < 4:
        expelled += 1
    if expelled > 1:
        break
    grade += 1
    sum_grades += current_grade

average_grade = sum_grades / grade
if expelled > 1:
    print(f"{name} has been excluded at {grade - 1} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
