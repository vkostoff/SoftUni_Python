pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]

maximum_health = int(input())
stalemate = True
command = input()

while not command == "Retire":
    command = command.split()
    
    if command[0] == "Fire":
        index1 = int(command[1])
        index2 = int(command[2])
        
        if index1 in range(0, len(war_ship) - 1):
            war_ship[index1] -= index2
            
            if war_ship[index1] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
                
    elif command[0] == "Defend":
        if int(command[1]) in range(0, len(pirate_ship)) and int(command[2]) in range(0, len(pirate_ship)):
            for i in range(int(command[1]), int(command[2]) + 1):
                pirate_ship[i] -= int(command[3])
                
            for i in pirate_ship:
                if i <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
                    
            if not stalemate:
                break
                
    elif command[0] == "Repair":
        if int(command[1]) in range(0, len(pirate_ship) - 1):
            if pirate_ship[int(command[1])] + int(command[2]) <= maximum_health:
                pirate_ship[int(command[1])] += int(command[2])
                
            else:
                pirate_ship[int(command[1])] = maximum_health
                
    elif command[0] == "Status":
        to_be_repaired = []
        
        for i in pirate_ship:
            if i < (maximum_health * 0.2):
                to_be_repaired.append(i)
                
        print(f"{len(to_be_repaired)} sections need repair.")

    command = input()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
