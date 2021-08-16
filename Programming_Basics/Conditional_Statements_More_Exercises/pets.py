from math import floor, ceil

days = int(input())
food = int(input())
dogfood_per_day = float(input())
catfood_per_day = float(input())
turtlefood_g = float(input())

turtlefood_per_day = turtlefood_g / 1000
total_food = (dogfood_per_day + catfood_per_day + turtlefood_per_day) * days

if food >= total_food:
    remaining_food = food - total_food
    print(f"{floor(remaining_food)} kilos of food left.")

else:
    food_needed = total_food - food
    print(f"{ceil(food_needed)} more kilos of food are needed.")
