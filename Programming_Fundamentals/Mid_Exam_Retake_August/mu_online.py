initial_health = 100
initial_bitcoins = 0

failed = False

rooms = input().split("|")
for room in rooms:
    command = room.split()
    if command[0] == "potion":
        if initial_health + int(command[1]) <= 100:
            initial_health += int(command[1])
            print(f"You healed for {int(command[1])} hp.")
        else:
            print(f"You healed for {100 - initial_health} hp.")
            initial_health = 100
        print(f"Current health: {initial_health} hp.")
    elif command[0] == "chest":
        initial_bitcoins += int(command[1])
        print(f"You found {int(command[1])} bitcoins.")
    else:
        initial_health -= int(command[1])
        if initial_health > 0:
            print(f"You slayed {command[0]}.")
        else:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {rooms.index(room) + 1}")
            failed = True
            break
if not failed:
    print("You've made it!""\n"f"Bitcoins: {initial_bitcoins}""\n"f"Health: {initial_health}")
