movie = input()
hall_type = input()
tickets_bought = int(input())
if movie == "A Star Is Born":
    if hall_type == "normal":
        price = 7.5
    elif hall_type == "luxury":
        price = 10.5
    elif hall_type == "ultra luxury":
        price = 13.5
elif movie == "Bohemian Rhapsody":
    if hall_type == "normal":
        price = 7.35
    elif hall_type == "luxury":
        price = 9.45
    elif hall_type == "ultra luxury":
        price = 12.75
elif movie == "Green Book":
    if hall_type == "normal":
        price = 8.15
    elif hall_type == "luxury":
        price = 10.25
    elif hall_type == "ultra luxury":
        price = 13.25
elif movie == "The Favourite":
    if hall_type == "normal":
        price = 8.75
    elif hall_type == "luxury":
        price = 11.55
    elif hall_type == "ultra luxury":
        price = 13.95
total = tickets_bought * price
print(f"{movie} -> {total:.2f} lv.")