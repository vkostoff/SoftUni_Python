days = int(input())
room_type = input()
rating = input()

nights = days - 1
price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18

elif room_type == "apartment":
    price_per_night = 25

elif room_type == "president apartment":
    price_per_night = 35

total_price = price_per_night * nights

if room_type == "apartment":

    if days < 10:
        total_price *= 0.70

    elif 10 <= days <= 15:
        total_price *= 0.65

    else:
        total_price *= 0.50

if room_type == "president apartment":

    if days < 10:
        total_price *= 0.90

    elif 10 <= days <= 15:
        total_price *= 0.85

    else:
        total_price *= 0.80

if rating == "positive":
    total_price *= 1.25

elif rating == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")
