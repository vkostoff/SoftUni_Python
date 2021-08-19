budget = int(input())
season = input()
fishers = int(input())
price = 0

if season == "Spring":
    price = 3000

elif season == "Summer" or season == "Autumn":
    price = 4200

elif season == "Winter":
    price = 2600

if fishers <= 6:
    price *= 0.9

elif 6 < fishers <= 11:
    price *= 0.85

elif fishers >= 12:
    price *= 0.75

if fishers % 2 == 0 and not season == "Autumn":
    price *= 0.95

if budget >= price:
    money_left = budget - price
    print(f"Yes! You have {money_left:.2f} leva left.")

else:
    money_needed = price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
