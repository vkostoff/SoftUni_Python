stash = {}

pair = []

command = input()
while not command == "stop":
    pair.append(command)
    if len(pair) == 2:
        if pair[0] not in stash:
            stash[pair[0]] = int(pair[1])
        else:
            stash[pair[0]] += int(pair[1])
        pair.clear()

    command = input()

for key, value in stash.items():
    print(f"{key} -> {value}")
