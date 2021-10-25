from math import ceil
fan_name = input()
budget = float(input())
beers_count = int(input())
chips_count = int(input())
beer_price = beers_count * 1.2
chips_price = chips_count * (beer_price * 0.45)
total_price = beer_price + ceil(chips_price)
if budget >= total_price:
    money_left = budget - total_price
    print(f"{fan_name} bought a snack and has {money_left:.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"{fan_name} needs {money_needed:.2f} more leva!")
