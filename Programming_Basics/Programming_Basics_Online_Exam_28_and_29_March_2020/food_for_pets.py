days_count = int(input())
total_food = float(input())
biscuits = 0
dog_eaten = 0
cat_eaten = 0
for days in range(1, days_count + 1):
    dog_per_day = int(input())
    cat_per_day = int(input())
    dog_eaten += dog_per_day
    cat_eaten += cat_per_day
    if days % 3 == 0:
        biscuits += (dog_per_day + cat_per_day) * 0.1
total_eaten = dog_eaten + cat_eaten

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten / total_food * 100:.2f}% of the food has been eaten.")
print(f"{dog_eaten / total_eaten * 100:.2f}% eaten from the dog.")
print(f"{cat_eaten / total_eaten * 100:.2f}% eaten from the cat.")
