flower_type = input()
flower_count = int(input())
budget = int(input())

price_per_unit = 0

if flower_type == "Roses":
    price_per_unit = 5

elif flower_type == "Dahlias":
    price_per_unit = 3.8

elif flower_type == "Tulips":
    price_per_unit = 2.8

elif flower_type == "Narcissus":
    price_per_unit = 3

elif flower_type == "Gladiolus":
    price_per_unit = 2.5

total_price = price_per_unit * flower_count

if flower_type == "Roses" and flower_count > 80:
    total_price *= 0.9

elif flower_type == "Dahlias" and flower_count > 90:
    total_price *= 0.85

elif flower_type == "Tulips" and flower_count > 80:
    total_price *= 0.85

elif flower_type == "Narcissus" and flower_count < 120:
    total_price *= 1.15

elif flower_type == "Gladiolus" and flower_count < 80:
    total_price *= 1.2

if total_price <= budget:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")

else:
    money_needed = total_price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
