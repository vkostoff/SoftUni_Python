budget = float(input())
season = input()

price = 0
stay = ""
place = ""

if budget <= 1000:
    stay = "Camp"
    
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.65
        
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.45
        
elif 1000 < budget <= 3000:
    stay = "Hut"
    
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.80
        
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.60
        
elif budget > 3000:
    stay = "Hotel"
    price = budget * 0.90
    
    if season == "Summer":
        place = "Alaska"
        
    elif season == "Winter":
        place = "Morocco"

print(f"{place} - {stay} - {price:.2f}")
