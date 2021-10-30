coffee = 0
need_sleep = False
command = input()
while command != "END":
    if command == "dog".lower() or command == "cat".lower() or command == "coding".lower()\
            or command == "movie".lower():
        coffee += 1
    elif command == "dog".upper() or command == "cat".upper() or command == "coding".upper()\
            or command == "movie".upper():
        coffee += 2
    if coffee > 5:
        need_sleep = True
        break
    command = input()
if need_sleep:
    print("You need extra sleep")
else:
    print(coffee)