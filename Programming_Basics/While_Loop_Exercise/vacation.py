money_needed = float(input())
money_available = float(input())
spending_counter = 0
total_days = 0
spending_too_many_days = False
while money_available < money_needed:
    action = input()
    current_sum = float(input())
    total_days += 1
    if action == "save":
        money_available += current_sum
        spending_counter = 0
    elif action == "spend":
        money_available -= current_sum
        spending_counter += 1
        if money_available < 0:
            money_available = 0
        if spending_counter == 5:
            spending_too_many_days = True
            break
if spending_too_many_days:
    print("You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")
