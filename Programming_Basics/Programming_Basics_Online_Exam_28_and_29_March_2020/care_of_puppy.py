food = int(input()) * 1000
command = input()

total_food = 0

while command != "Adopted":
    daily_food = int(command)
    total_food += daily_food
    command = input()
    
if total_food <= food:
    leftover = food - total_food
    print(f"Food is enough! Leftovers: {leftover} grams.")
    
else:
    needed = total_food - food
    print(f"Food is not enough. You need {needed} grams more.")
