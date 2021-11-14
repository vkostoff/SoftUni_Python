rows = int(input())
ships = []
destroyed = 0
for r in range(rows):
    ships.append([int(x) for x in input().split(" ")])
attack = input().split(" ")
for el in attack:
    el.split("-")
    row = int(el[0])
    column = int(el[2])
    ships[row][column] -= 1
    if ships[row][column] == 0:
        destroyed += 1
print(destroyed)