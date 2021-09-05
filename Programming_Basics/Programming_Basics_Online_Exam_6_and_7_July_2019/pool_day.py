from math import ceil
people = int(input())
tax = float(input())
price_per_lounge = float(input())
price_per_umbrella = float(input())
all_people_tax = people * tax
all_lounge_price = ceil(people * 0.75) * price_per_lounge
all_umbrella_price = ceil(people / 2) * price_per_umbrella
total = all_umbrella_price + all_lounge_price + all_people_tax
print(f"{total:.2f} lv.")
