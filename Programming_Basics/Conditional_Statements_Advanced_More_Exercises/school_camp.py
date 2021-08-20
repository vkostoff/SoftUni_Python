season = input()
group = input()
students = int(input())
accommodations = int(input())

price_per_night = 0
sport = ""

if group == "boys":
    
    if season == "Winter":
        sport = "Judo"
        price_per_night = 9.60
        
    elif season == "Spring":
        sport = "Tennis"
        price_per_night = 7.2
        
    elif season == "Summer":
        sport = "Football"
        price_per_night = 15
        
elif group == "girls":
    
    if season == "Winter":
        sport = "Gymnastics"
        price_per_night = 9.60
        
    elif season == "Spring":
        sport = "Athletics"
        price_per_night = 7.2
        
    elif season == "Summer":
        sport = "Volleyball"
        price_per_night = 15
        
elif group == "mixed":
    
    if season == "Winter":
        sport = "Ski"
        price_per_night = 10
        
    elif season == "Spring":
        sport = "Cycling"
        price_per_night = 9.5
        
    elif season == "Summer":
        sport = "Swimming"
        price_per_night = 20
        
total_accommodation = (accommodations * students) * price_per_night

if students >= 50:
    total_accommodation *= 0.5
    
elif 50 > students >= 20:
    total_accommodation *= 0.85
    
elif 20 > students >= 10:
    total_accommodation *= 0.95

print(f"{sport} {total_accommodation:.2f} lv.")
