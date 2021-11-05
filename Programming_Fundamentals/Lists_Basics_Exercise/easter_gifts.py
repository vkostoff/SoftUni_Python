gifts_list = list(input().split(sep=" "))
command = input()
while not command == "No Money":
    command = list(command.split(sep=" "))
    if "OutOfStock" in command:
        for i in range(0, len(gifts_list)):
            if gifts_list[i] == command[1]:
                gifts_list[i] = "None"
    elif "Required" in command:
        if 0 < int(command[2]) < len(gifts_list):
            gifts_list[int(command[2])] = command[1]
    elif "JustInCase" in command:
        gifts_list[-1] = command[1]
    command = input()
for j in gifts_list:
    if "None" in gifts_list:
        gifts_list.remove("None")
print(*gifts_list)
