movie_budget = float(input())
people_count = int(input())
clothing_per_person_cost = float(input())

decor_cost = movie_budget * 0.10
all_clothing = people_count * clothing_per_person_cost

if people_count > 150:
    all_clothing *= 0.9

expenses = decor_cost + all_clothing
money_left = movie_budget - expenses
money_needed = expenses - movie_budget

if expenses > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")

if expenses <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")


