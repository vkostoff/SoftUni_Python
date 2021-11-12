targets_sequence = [int(x) for x in input().split(" ")]

while True:
    tokens = input().split(" ")
    command = tokens[0]
    index = 0
    value = 0
    
    if command == "Shoot":
        index = command[1]
        value = command[2]
        
        if int(command[1]) < len(targets_sequence):
            targets_sequence[int(command[1])] -= int(command[2])
            if targets_sequence[int(command[1])] <= 0:
                targets_sequence.pop(int(command[1]))

    elif "Add" in command:
        if int(command[1]) < len(targets_sequence):
            targets_sequence.insert(int(command[1]), int(command[2]))
        else:
            print("Invalid placement!")

    elif "Strike" in command:
        lower_radius = int(command[1]) - int(command[2])
        upper_radius = int(command[1]) + int(command[2])
        
        if lower_radius >= 0 and upper_radius < len(targets_sequence):
            del targets_sequence[lower_radius:upper_radius + 1]
            
        else:
            print("Strike missed!")
            
targets_sequence = [str(x) for x in targets_sequence]
print("|".join(targets_sequence))
