treasure_chest_state = [x for x in input().split("|")]
command = input()

while not command == "Yohoho!":
    command = command.split()
    
    if "Loot" in command:
        for i in range(1, len(command)):
            if command[i] not in treasure_chest_state:
                treasure_chest_state.insert(0, command[i])
                
    elif "Drop" in command:
        index = int(command[1])
        
        if 0 <= index < len(treasure_chest_state):
            treasure_chest_state.append(treasure_chest_state.pop(index))
            
    elif "Steal" in command:
        stolen_items = treasure_chest_state[:(-1 - int(command[1])):-1]
        del treasure_chest_state[:(-1 - int(command[1])):-1]
        
        stolen_items.reverse()
        print(", ".join(stolen_items))
    command = input()

if len(treasure_chest_state) > 0:
    average_treasure_gain = sum([len(x) for x in treasure_chest_state]) / len(treasure_chest_state)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
    
else:
    print("Failed treasure hunt.")
