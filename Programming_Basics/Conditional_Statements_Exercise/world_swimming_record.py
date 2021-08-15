current_record = float(input())
distance = float(input())
seconds_per_meter = float(input())

slow_down = (distance // 15) * 12.5
attempt = (distance * seconds_per_meter) + slow_down

if attempt >= current_record:
    difference = attempt - current_record
    print(f"No, he failed! He was {difference:.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {attempt:.2f} seconds.")
