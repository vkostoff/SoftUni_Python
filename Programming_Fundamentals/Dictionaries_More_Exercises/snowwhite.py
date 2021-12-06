dwarfs = {}
colors = {}

command = input()
while not command == "Once upon a time":
    name, color, physics = command.split(" <:> ")
    physics = int(physics)
    if name not in dwarfs:
        dwarfs[name] = [color, physics]

        if color not in colors:
            colors[color] = 0
        colors[color] += 1

    elif name in dwarfs and not dwarfs[name][0] == color:
        dwarfs[f"{name} "] = [color, physics]

        if color not in colors:
            colors[color] = 0
        colors[color] += 1

    elif physics > dwarfs[name][1]:
        dwarfs[name] = [color, physics]
    command = input()

ordered_dwarfs = {d: i for d, i in sorted(dwarfs.items(), key=lambda x: (-x[1][1], -colors[x[1][0]]))}

for k, v in ordered_dwarfs.items():
    print(f"({v[0]}) {str(k).strip()} <-> {v[1]}")