price_over_20 = float(input())
luggage_kg = float(input())
days_to_trip = int(input())
luggage_count = int(input())

if luggage_kg < 10:
    price_over_20 *= 0.20
    
elif 10 <= luggage_kg <= 20:
    price_over_20 *= 0.5
    
else:
    price_over_20

luggage_price = price_over_20

if days_to_trip > 30:
    luggage_price *= 1.1
    
elif 7 <= days_to_trip <= 30:
    luggage_price *= 1.15
    
else:
    luggage_price *= 1.4

total_price = luggage_price * luggage_count

print(f"The total price of bags is: {total_price:.2f} lv.")
