menu = {}

command = input()
while not command == "buy":
    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in menu:
        menu[product] = [price, quantity]
    else:
        if not price == menu[product][0]:
            menu[product][0] = price
        menu[product][1] += quantity
    command = input()

for key, value in menu.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")