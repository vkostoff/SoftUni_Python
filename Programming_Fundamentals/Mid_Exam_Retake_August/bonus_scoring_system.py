students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_lectures = 0

for i in range(students):
    attendances = int(input())
    total_bonus = (attendances / lectures) * (5 + additional_bonus)
    
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_lectures = attendances
        
print(f"Max Bonus: {round(max_bonus)}.""\n"f"The student has attended {max_lectures} lectures.")
