budget = float(input())
fuel_needed = float(input())
week_day = input()
fuel_price = fuel_needed * 2.1
total_price = fuel_price + 100
if week_day == "Saturday":
    total_price *= 0.9
elif week_day == "Sunday":
    total_price *= 0.8
if budget >= total_price:
    money_left = budget - total_price
    print(f"Safari time! Money left: {money_left:.2f} lv. ")
elif budget < total_price:
    money_needed = total_price - budget
    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")
