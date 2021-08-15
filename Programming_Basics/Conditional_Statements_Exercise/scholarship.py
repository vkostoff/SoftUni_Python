income = float(input())
average_grade = float(input())
min_salary = float(input())

social_scholarship = min_salary * 0.35
excellent_scholarship = average_grade * 25

if average_grade >= 5.5:

    if income < min_salary and social_scholarship > excellent_scholarship:
        print(f"You get a Social scholarship {int(social_scholarship)} BGN")

    else:
        print(f"You get a scholarship for excellent results {int(excellent_scholarship)} BGN")

elif income < min_salary and average_grade > 4.5:
    print(f"You get a Social scholarship {int(social_scholarship)} BGN")

else:
    print("You cannot get a scholarship!")
