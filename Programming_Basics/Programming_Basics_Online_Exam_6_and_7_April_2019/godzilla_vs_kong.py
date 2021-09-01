budget = float(input())
people = int(input())
person_outfit = float(input())
decor = budget * 0.1
price_outfit = person_outfit * people
if people > 150:
    price_outfit *= 0.9
all_money = decor + price_outfit
if budget >= all_money:
    money_left = budget - all_money
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

else:
    money_needed = all_money - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
