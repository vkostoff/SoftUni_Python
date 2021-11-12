inventory = input().split(", ")
string = input()
while not string == "Craft!":
    string = string.split(" - ")
    command = string[0]
    item = string[1]
    if command == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif command == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif command == "Combine Items":
        item = item.split(":")
        if item[0] in inventory:
            index = inventory.index(item[0]) + 1
            inventory.insert(index, item[1])
    elif command == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    string = input()
print(", ".join(inventory))