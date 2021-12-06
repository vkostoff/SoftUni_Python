dragons = {}

default_health, default_damage, default_armor = 250, 45, 10

number = int(input())
for n in range(number):
    dragon_type, name, damage, health, armor = input().split()

    if health == "null":
        health = default_health
    if damage == "null":
        damage = default_damage
    if armor == "null":
        armor = default_armor

    if dragon_type not in dragons:
        dragons[dragon_type] = {}
    dragons[dragon_type][name] = [int(damage), int(health), int(armor)]

for k, v in dragons.items():
    dragons[k] = dict(sorted(dragons[k].items(), key=lambda x: x[0]))
    avg_damage = 0
    avg_health = 0
    avg_armor = 0
    for key, value in v.items():
        avg_damage += value[0]
        avg_health += value[1]
        avg_armor += value[2]
    print(f"{k}::({avg_damage/len(v):.2f}/{avg_health/len(v):.2f}/{avg_armor/len(v):.2f})")
    for a, b in dragons[k].items():
        print(f"-{a} -> damage: {b[0]}, health: {b[1]}, armor: {b[2]}")