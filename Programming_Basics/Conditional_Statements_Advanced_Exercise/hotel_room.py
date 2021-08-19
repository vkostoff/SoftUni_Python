month = input()
nights = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_apartment = 65
    price_studio = 50

elif month == "June" or month == "September":
    price_apartment = 68.70
    price_studio = 75.20

elif month == "July" or month == "August":
    price_apartment = 77
    price_studio = 76

if (month == "May" or month == "October") and 14 >= nights > 7:
    price_studio *= 0.95

elif (month == "May" or month == "October") and nights > 14:
    price_studio *= 0.70

elif (month == "June" or month == "September") and nights > 14:
    price_studio *= 0.80

if nights > 14:
    price_apartment *= 0.90

apartment = price_apartment * nights
studio = price_studio * nights

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
