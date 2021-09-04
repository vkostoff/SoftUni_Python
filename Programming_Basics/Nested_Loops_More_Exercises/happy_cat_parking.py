days = int(input())
hours = int(input())
counter = 0
total_price = 0
for d in range(1, days + 1):
    counter += 1
    daily_price = 0
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            daily_price += 2.5
        elif d % 2 != 0 and h % 2 == 0:
            daily_price += 1.25
        else:
            daily_price += 1
    print(f"Day: {counter} - {daily_price:.2f} leva")
    total_price += daily_price
print(f"Total: {total_price:.2f} leva")