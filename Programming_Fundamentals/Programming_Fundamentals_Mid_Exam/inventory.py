inventory = input().split(", ")
command = input()
while not command == "Craft!":
    command = command.split(" - ")
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        item = item.split(":")
        if item[0] in inventory:
            inventory.insert(inventory.index(item[0]) + 1, item[1])
    elif action == "Renew":
        if item in inventory:
            inventory.insert(len(inventory), item)
            inventory.remove(item)
    command = input()
print(", ".join(inventory))