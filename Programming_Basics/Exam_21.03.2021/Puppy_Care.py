food_bought = int(input())
food_bought_grams = food_bought * 1000

command = input()

while command != "Adopted":
    grams_eaten_per_meal = int(command)
    food_bought_grams -= grams_eaten_per_meal
    command = input()
    
if food_bought_grams < 0:
    print(f"Food is not enough. You need {abs(food_bought_grams)} grams more." )
else:
    print(f"Food is enough! Leftovers: {food_bought_grams} grams." )
