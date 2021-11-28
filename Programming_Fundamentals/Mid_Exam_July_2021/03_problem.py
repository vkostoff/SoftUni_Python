chat_history = []
command = input()
while not command == "end":
    command = command.split()
    if command[0] == "Chat":
        chat_history.append(command[1])
    elif command[0] == "Delete":
        if command[1] in chat_history:
            chat_history.remove(command[1])
    elif command[0] == "Edit":
        if command[1] in chat_history:
            index = chat_history.index(command[1])
            chat_history.remove(command[1])
            chat_history.insert(int(index), command[2])
    elif command[0] == "Pin":
        if command[1] in chat_history:
            chat_history.remove(command[1])
            chat_history.append(command[1])
    elif command[0] == "Spam":
        chat_history.extend(command[1:])
    command = input()

for i in chat_history:
    print(i)