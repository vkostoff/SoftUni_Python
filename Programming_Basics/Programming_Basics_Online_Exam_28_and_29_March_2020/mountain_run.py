record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_m = float(input())

slow_down = (distance_in_meters // 50) * 30
attempt = distance_in_meters * time_in_seconds_per_m
current_attempt = attempt + round(slow_down)

if current_attempt < record_in_seconds:
    print(f"Yes! The new record is {current_attempt:.2f} seconds.")
    
else:
    not_enough = current_attempt - record_in_seconds
    print(f"No! He was {not_enough:.2f} seconds slower.")
