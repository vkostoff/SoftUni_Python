budget = float(input())
video_count = int(input())
processor_count = int(input())
ram = int(input())
video_price = 250 * video_count
processor_price = processor_count * (video_price * 0.35)
ram_price = ram * (video_price * 0.1)
total_price = video_price + processor_price + ram_price
if processor_count < video_count:
    total_price *= 0.85
if budget >= total_price:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")
