budget = float(input())
category = input()
people = int(input())
transport = 0
price = 0

if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
elif people >= 50:
    transport = budget * 0.25

total_money = budget - transport

if category == "VIP":
    price = 499.99
elif category == "Normal":
    price = 249.99

total_price = price * people

if total_money >= total_price:
    difference = abs(total_money - total_price)
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    difference = total_price - total_money
    print(f"Not enough money! You need {difference:.2f} leva.")
