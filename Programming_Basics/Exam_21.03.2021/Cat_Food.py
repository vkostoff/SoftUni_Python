small_cats = 0
big_cats = 0
huge_cats = 0
total_food = 0
cats = int(input())
for cats in range(1, cats + 1):
    food_per_cat = float(input())
    total_food += food_per_cat
    if 100 <= food_per_cat < 200:
        small_cats += 1
    elif 200 <= food_per_cat < 300:
        big_cats += 1
    elif 300 <= food_per_cat < 400:
        huge_cats += 1
total_price = (total_food / 1000) * 12.45
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")
