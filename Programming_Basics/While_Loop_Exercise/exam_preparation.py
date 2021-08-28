low_grades_allowed = int(input())

all_problems = 0
low_grades = 0
all_grades = 0
problem = ""

command = input()

while command != "Enough":
    problem_name = command
    problem = problem_name
    
    grade = int(input())
    
    all_grades += grade
    all_problems += 1
    
    if grade <= 4:
        low_grades += 1
        
    if low_grades == low_grades_allowed:
        print(f"You need a break, {low_grades} poor grades.")
        break
        
    command = input()
    
else:
    average_grade = all_grades / all_problems
    
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {all_problems}")
    print(f"Last problem: {problem}")
