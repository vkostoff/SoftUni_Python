from math import ceil

average_speed = float(input())
fuel_needed = float(input())

total_distance = 384400 * 2
total_hours = total_distance / average_speed + 3
fuel = (fuel_needed * total_distance) / 100

print(ceil(total_hours))
print(int(fuel))
