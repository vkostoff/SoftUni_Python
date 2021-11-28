weapon_parts = input().split("|")

command = input()
while not command == "Done":
    command = command.split()
    if command[0] == "Add":
        if 0 <= int(command[2]) < len(weapon_parts):
            weapon_parts.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if 0 <= int(command[1]) < len(weapon_parts):
            weapon_parts.pop(int(command[1]))
    elif command[0] == "Check":
        if command[1] == "Even":
            even_list = []
            for i in range(len(weapon_parts)):
                if i % 2 == 0:
                    even_list.append(weapon_parts[i])
            print(" ".join(even_list))
        elif command[1] == "Odd":
            odd_list = []
            for i in range(len(weapon_parts)):
                if not i % 2 == 0:
                    odd_list.append(weapon_parts[i])
            print(" ".join(odd_list))
    command = input()

print(f"You crafted {''.join(weapon_parts)}!")
