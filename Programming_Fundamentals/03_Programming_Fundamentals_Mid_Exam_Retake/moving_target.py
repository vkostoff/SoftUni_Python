targets = [int(x) for x in input().split(" ")]
token = input()
while not token == "End":
    token = token.split(" ")
    command = token[0]
    index = int(token[1])
    power = int(token[2])
    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, power)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if 0 <= index < len(targets):
            before = index - power
            after = index + power + 1
            if before >= 0 and after < len(targets):
                del targets[before:after]
            else:
                print("Strike missed!")

    token = input()
targets = [str(y) for y in targets]
print("|".join(targets))