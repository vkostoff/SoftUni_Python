first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

hours = 0
students_per_hour = first_employee + second_employee + third_employee

while students_count > 0:
    students_count -= students_per_hour
    hours += 1
    
    if hours % 4 == 0:
        hours += 1
        
print(f"Time needed: {hours}h.")
