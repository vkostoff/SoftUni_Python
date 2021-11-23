targets = [int(x) for x in input().split()]
targets_shot = 0
token = input()

while not token == "End":
    index = int(token)
    
    if index < len(targets) and not targets[index] == -1:
        current_integer = targets[index]
        targets[index] = -1
        targets_shot += 1
        
        for i in range(len(targets)):
            if not targets[i] == -1 and targets[i] > current_integer:
                targets[i] -= current_integer
                
            elif not targets[i] == -1 and targets[i] <= current_integer:
                targets[i] += current_integer
                
    token = input()
    
targets = [str(y) for y in targets]

print(f"Shot targets: {targets_shot} -> {' '.join(targets)}")
