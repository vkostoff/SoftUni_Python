eggs_first_player = int(input())
eggs_second_player = int(input())
game_over = False

command = input()
while command != "End of battle":
    
    if command == "one":
        eggs_second_player -= 1
        
    elif command == "two":
        eggs_first_player -= 1
        
    if eggs_first_player == 0 or eggs_second_player == 0:
        game_over = True
        break
        
    command = input()
    
if eggs_first_player == 0:
    print(f"Player one is out of eggs. Player two has {eggs_second_player} eggs left.")
    
elif eggs_second_player == 0:
    print(f"Player two is out of eggs. Player one has {eggs_first_player} eggs left.")
    
else:
    print(f"Player one has {eggs_first_player} eggs left.")
    print(f"Player two has {eggs_second_player} eggs left.")
