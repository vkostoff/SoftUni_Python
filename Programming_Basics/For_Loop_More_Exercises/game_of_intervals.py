game_moves = int(input())

points = 0
invalid_numbers = 0
numbers_0_to_9 = 0
numbers_10_to_19 = 0
numbers_20_to_29 = 0
numbers_30_to_39 = 0
numbers_40_to_50 = 0

for moves in range(1, game_moves + 1):
    move = int(input())
    
    if 0 <= move <= 9:
        points += move * 0.2
        numbers_0_to_9 += 1
        
    elif 10 <= move <= 19:
        points += move * 0.3
        numbers_10_to_19 += 1
        
    elif 20 <= move <= 29:
        points += move * 0.4
        numbers_20_to_29 += 1
        
    elif 30 <= move <= 39:
        points += 50
        numbers_30_to_39 += 1
        
    elif 40 <= move <= 50:
        points += 100
        numbers_40_to_50 += 1
        
    else:
        points /= 2
        invalid_numbers += 1

total_numbers = numbers_0_to_9 + numbers_10_to_19 + numbers_20_to_29 + numbers_30_to_39 + numbers_40_to_50\
                + invalid_numbers

print(f"{points:.2f}")
print(f"From 0 to 9: {numbers_0_to_9 / game_moves * 100:.2f}%")
print(f"From 10 to 19: {numbers_10_to_19 / game_moves * 100:.2f}%")
print(f"From 20 to 29: {numbers_20_to_29 / game_moves * 100:.2f}%")
print(f"From 30 to 39: {numbers_30_to_39 / game_moves * 100:.2f}%")
print(f"From 40 to 50: {numbers_40_to_50 / game_moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / game_moves * 100:.2f}%")
