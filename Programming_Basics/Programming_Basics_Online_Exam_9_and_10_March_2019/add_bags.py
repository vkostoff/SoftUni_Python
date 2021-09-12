luggage_price_over_20kg = float(input())
luggage_kg = float(input())
days_till_travel = int(input())
luggage_count = int(input())
if luggage_kg > 20:
    luggage_price = luggage_price_over_20kg * luggage_count
elif 10 <= luggage_kg <= 20:
    luggage_price = (luggage_price_over_20kg * 0.5) * luggage_count
else:
    luggage_price = (luggage_price_over_20kg * 0.2) * luggage_count
if days_till_travel > 30:
    luggage_price *= 1.1
elif 7 <= days_till_travel <= 30:
    luggage_price *= 1.15
else:
    luggage_price *= 1.40
print(f"The total price of bags is: {luggage_price:.2f} lv. ")