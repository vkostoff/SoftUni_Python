journal = input().split(", ")
command = input()
while not command == "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in journal:
            journal.append(command[1])
    elif command[0] == "Drop":
        if command[1] in journal:
            journal.remove(command[1])
    elif command[0] == "Combine Items":
        items = command[1].split(":")
        if items[0] in journal:
            journal.insert(journal.index(items[0]) + 1, items[1])
    elif command[0] == "Renew":
        if command[1] in journal:
            journal.remove(command[1])
            journal.append(command[1])
    command = input()

print(", ".join(journal))