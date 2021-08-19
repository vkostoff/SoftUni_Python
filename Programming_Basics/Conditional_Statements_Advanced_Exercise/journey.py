budget = float(input())
season = input()

price = 0

accommodation = ""
destination = ""

if season == "summer":
    accommodation = "Camp"

elif season == "winter":
    accommodation = "Hotel"

if budget <= 100 and season == "summer":
    destination = "Bulgaria"
    price = budget * 0.30

elif 100 < budget <= 1000 and season == "summer":
    destination = "Balkans"
    price = budget * 0.40

elif budget <= 100 and season == "winter":
    destination = "Bulgaria"
    price = budget * 0.70

elif 100 < budget <= 1000 and season == "winter":
    destination = "Balkans"
    price = budget * 0.80

elif budget > 1000 and (season == "winter" or season == "summer"):
    accommodation = "Hotel"
    destination = "Europe"
    price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")