party_size = int(input())
days = int(input())

coins = 50 * days

for day in range(1, days + 1):
    
    if day % 10 == 0:
        party_size -= 2
        
    if day % 15 == 0:
        party_size += 5
        coins += (party_size * 18)
        
    if day % 3 == 0:
        coins -= (party_size * 3)
        
    elif day % 5 == 0:
        coins += (party_size * 20)
        
    coins -= party_size * 2
    
coins_per_companion = coins / party_size

print(f"{party_size} companions received {int(coins_per_companion)} coins each.")
