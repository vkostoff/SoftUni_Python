initial_list = input().split("!")
token = input()
while not token == "Go Shopping!":
    token = token.split()
    command = token[0]
    item = token[1]
    if command == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)
    elif command == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)
    elif command == "Correct":
        if item in initial_list:
            initial_list.insert(initial_list.index(item), token[2])
            initial_list.remove(item)
    elif command == "Rearrange":
        if item in initial_list:
            x = initial_list.pop(initial_list.index(item))
            initial_list.append(x)
    token = input()

print(", ".join(initial_list))