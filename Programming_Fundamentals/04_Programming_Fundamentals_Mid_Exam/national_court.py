first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_people = int(input())

hours = 1

while True:
    if total_people == 0:
        hours = 0
        break
        
    elif (first_employee + second_employee + third_employee) < total_people:
        total_people -= (first_employee + second_employee + third_employee)
        hours += 1
        
        if hours % 4 == 0:
            hours += 1
            
    else:
        break

print(f"Time needed: {hours}h.")
