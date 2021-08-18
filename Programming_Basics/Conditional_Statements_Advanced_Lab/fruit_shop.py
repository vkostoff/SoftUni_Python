fruit = input()
day = input()
quantity = float(input())

price = 0

if fruit == "banana":

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.50

    elif day == "Saturday" or day == "Sunday":
        price = 2.70

elif fruit == "apple":

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.20

    elif day == "Saturday" or day == "Sunday":
        price = 1.25

elif fruit == "orange":

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 0.85

    elif day == "Saturday" or day == "Sunday":
        price = 0.90

elif fruit == "grapefruit":

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.45

    elif day == "Saturday" or day == "Sunday":
        price = 1.60

elif fruit == "kiwi":

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.70

    elif day == "Saturday" or day == "Sunday":
        price = 3.00

elif fruit == "pineapple":

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 5.50

    elif day == "Saturday" or day == "Sunday":
        price = 5.60

elif fruit == "grapes":

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 3.85

    elif day == "Saturday" or day == "Sunday":
        price = 4.20

total_price = quantity * price

if price == 0:
    print("error")

else:
    print(f"{total_price:.2f}")
