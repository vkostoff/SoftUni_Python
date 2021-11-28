experience_needed = float(input())
count_of_battles = int(input())
experience_gained = 0
counter = 0
success = False

for i in range(1, count_of_battles + 1):
    current_experience = float(input())
    if i % 3 == 0:
        experience_gained += (current_experience * 1.15)
        counter += 1
    elif i % 5 == 0:
        experience_gained += (current_experience * 0.9)
        counter += 1
    elif i % 15 == 0:
        experience_gained += (current_experience * 1.05)
        counter += 1
    else:
        experience_gained += current_experience
        counter += 1
    if experience_gained >= experience_needed:
        success = True
        break

if success:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    difference = experience_needed - experience_gained
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")