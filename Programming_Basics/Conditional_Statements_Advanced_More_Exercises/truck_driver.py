season = input()
km_per_month = float(input())
award = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        award = 0.75
    elif season == "Summer":
        award = 0.90
    elif season == "Winter":
        award = 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        award = 0.95
    elif season == "Summer":
        award = 1.10
    elif season == "Winter":
        award = 1.25
elif 10000 < km_per_month <= 20000:
    award = 1.45

salary = ((award * km_per_month) * 4) * 0.90

print(f"{salary:.2f}")
