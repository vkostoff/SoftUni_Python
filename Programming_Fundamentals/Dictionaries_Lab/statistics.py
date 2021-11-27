products = {}

command = input()
while not command == "statistics":
    command = command.split(": ")
    if command[0] not in products:
        products[command[0]] = int(command[1])
    else:
        products[command[0]] += int(command[1])
    command = input()

print("Products in stock:")

for (key, value) in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")