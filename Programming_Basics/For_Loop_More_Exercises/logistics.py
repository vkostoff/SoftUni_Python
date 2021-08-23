loads_count = int(input())
price_per_ton = 0
total_loads = 0
bus = 0
truck = 0
train = 0

for loads in range(1, loads_count + 1):
    load_tonnage = int(input())
    if load_tonnage <= 3:
        bus += load_tonnage
        price_per_ton += 200 * load_tonnage
        total_loads += load_tonnage
    if 4 <= load_tonnage <= 11:
        truck += load_tonnage
        price_per_ton += 175 * load_tonnage
        total_loads += load_tonnage
    if load_tonnage >= 12:
        train += load_tonnage
        price_per_ton += 120 * load_tonnage
        total_loads += load_tonnage

average_price = price_per_ton / total_loads
bus_percentage = bus / total_loads * 100
truck_percentage = truck / total_loads * 100
train_percentage = train / total_loads * 100

print(f"{average_price:.2f}")
print(f"{bus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
