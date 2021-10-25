month = input()
hours_spent = int(input())
people_count = int(input())
day_time = input()
price = 0

if month == "march" or month == "april" or month == "may":
    if day_time == "day":
        price = 10.5
    elif day_time == "night":
        price = 8.4
elif month == "june" or month == "july" or month == "august":
    if day_time == "day":
        price = 12.6
    elif day_time == "night":
        price = 10.2

if people_count >= 4:
    price *= 0.9
if hours_spent >= 5:
    price *= 0.5

total_price = people_count * hours_spent * price


print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")