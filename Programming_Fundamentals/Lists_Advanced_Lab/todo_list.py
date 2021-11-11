notes = ["0"] * 20

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0]) + 1
    note = tokens[1]
    notes.pop(priority + 2)
    notes.insert(priority, note)

result = [element for element in notes if element != "0"]
print(result)