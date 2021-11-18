health = 100
bitcoins = 0
dead = False

rooms = input().split("|")

for room in rooms:
    element = room.split()
    command = element[0]
    number = int(element[1])
    
    if command == "potion":
        if number + health > 100:
            amount = 100 - health
            print(f"You healed for {amount} hp.")
            health = 100
            print(f"Current health: {health} hp.")
            
        else:
            health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
            
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
        
    else:
        health -= number
        
        if health > 0:
            print(f"You slayed {command}.")
            
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room) + 1}")
            dead = True
            break

if not dead:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
