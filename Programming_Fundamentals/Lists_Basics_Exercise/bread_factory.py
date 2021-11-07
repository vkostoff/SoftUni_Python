energy = 100
coins = 100

current_event = []
events = input().split(sep="|")
broke = False

for event in events:
    current_event = event.split(sep="-")
    
    if "rest" in current_event:
        if energy + int(current_event[1]) <= 100:
            energy += int(current_event[1])
            print(f"You gained {int(current_event[1])} energy.")
            print(f"Current energy: {energy}.")
            
        else:
            current_energy = 100 - energy
            energy = 100
            print(f"You gained {current_energy} energy.")
            print(f"Current energy: {energy}.")
            
    elif "order" in current_event:
        if energy >= 30:
            coins += int(current_event[1])
            energy -= 30
            print(f"You earned {int(current_event[1])} coins.")
            
        else:
            energy += 50
            print("You had to rest!")
            
    else:
        if coins - int(current_event[1]) > 0:
            coins -= int(current_event[1])
            print(f"You bought {current_event[0]}.")
            
        else:
            print(f"Closed! Cannot afford {current_event[0]}.")
            broke = True
            break
            
if not broke:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
