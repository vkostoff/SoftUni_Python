budget = float(input())
season = input()
price = 0
vehicle_class = ""
vehicle_type = ""

if budget <= 100:
    vehicle_class = "Economy class"
    if season == "Summer":
        vehicle_type = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        vehicle_type = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    vehicle_class = "Compact class"
    vehicle_type = "Cabrio"
    if season == "Summer":
        price = budget * 0.45
    elif season == "Winter":
        vehicle_type = "Jeep"
        price = budget * 0.80
elif budget > 500:
    vehicle_class = "Luxury class"
    vehicle_type = "Jeep"
    if season == "Summer" or season == "Winter":
        price = budget * 0.90
print(vehicle_class)
print(f"{vehicle_type} - {price:.2f}")