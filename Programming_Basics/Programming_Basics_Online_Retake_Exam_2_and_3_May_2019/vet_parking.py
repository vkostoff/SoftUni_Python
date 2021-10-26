days_count = int(input())
hours_per_day = int(input())
to_be_paid = 0
daily = 0
counter = 0
for days in range(1, days_count + 1):
    for hours in range(1, hours_per_day + 1):
        if days % 2 == 0 and hours % 2 != 0:
            to_be_paid += 2.5
            daily += 2.5
        elif days % 2 != 0 and hours % 2 == 0:
            to_be_paid += 1.25
            daily += 1.25
        else:
            to_be_paid += 1
            daily += 1
    counter += 1
    print(f"Day: {counter} - {daily:.2f} leva")
    daily = 0
print(f"Total: {to_be_paid:.2f} leva")