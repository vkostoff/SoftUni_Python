inventory = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}

collected = False

while not collected:
    materials = input().lower()
    materials = materials.split()

    for i in range(0, len(materials), 2):
        key = materials[i + 1]
        value = int(materials[i])
        if key not in inventory:
            if key not in junk:
                junk[key] = value
            else:
                junk[key] += value
        else:
            inventory[key] += value
            if inventory[key] >= 250:
                for k, v in inventory.items():
                    if inventory[k] >= 250:
                        if k == "motes":
                            print("Dragonwrath obtained!")
                        elif k == "shards":
                            print("Shadowmourne obtained!")
                        elif k == "fragments":
                            print("Valanyr obtained!")
                inventory[key] -= 250
                collected = True
                break

sorted_inventory = dict(sorted(inventory.items(), key=lambda x: (-x[1], x[0])))
sorted_junk = dict(sorted(junk.items(), key=lambda x: x[0]))

for k, v in sorted_inventory.items():
    print(f"{k}: {v}")

for a, b in sorted_junk.items():
    print(f"{a}: {b}")