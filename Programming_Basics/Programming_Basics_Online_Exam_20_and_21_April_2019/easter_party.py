guests = int(input())
price_per_guest = float(input())
budget = float(input())
if 10 <= guests <= 15:
    price_per_guest *= 0.85
elif 15 < guests <= 20:
    price_per_guest *= 0.8
elif guests > 20:
    price_per_guest *= 0.75
cake_price = budget * 0.1
total = (price_per_guest * guests) + cake_price
if budget >= total:
    money_left = budget - total
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    money_needed = total - budget
    print(f"No party! {money_needed:.2f} leva needed.")