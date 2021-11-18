students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

best_bonus = 0
lectures = 0

for i in range(students_count):
    attendances = int(input())
    total_bonus = round(attendances / lectures_count * (5 + additional_bonus))
    
    if total_bonus > best_bonus:
        best_bonus = total_bonus
        lectures = attendances

print(f"Max Bonus: {round(best_bonus)}.")
print(f"The student has attended {lectures} lectures.")
