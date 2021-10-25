games_sold = int(input())

hearthstone_count = 0
fortnite_count = 0
overwatch_count = 0
others_count = 0

for games in range(1, games_sold + 1):
    game_name = input()
    
    if game_name == "Hearthstone":
        hearthstone_count += 1
        
    elif game_name == "Fornite":
        fortnite_count += 1
        
    elif game_name == "Overwatch":
        overwatch_count += 1
        
    else:
        others_count += 1
        
hearthstone_percentage = hearthstone_count / games_sold * 100
fortnite_percentage = fortnite_count / games_sold * 100
overwatch_percentage = overwatch_count / games_sold * 100
others_percentage = others_count / games_sold * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fortnite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")
