database = {}

commands_number = int(input())

for i in range(commands_number):
    command = input().split()
    if command[0] == "register":
        if command[1] in database:
            print(f"ERROR: already registered with plate number {command[2]}")
        else:
            database[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    elif command[0] == "unregister":
        if command[1] not in database:
            print(f"ERROR: user {command[1]} not found")
        else:
            del database[command[1]]
            print(f"{command[1]} unregistered successfully")

for k, v in database.items():
    print(f"{k} => {v}")