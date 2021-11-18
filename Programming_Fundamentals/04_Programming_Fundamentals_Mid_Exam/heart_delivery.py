neighborhood = [int(x) for x in input().split("@")]
current_position = 0
token = input()
while not token == "Love!":
    token = token.split()
    command = token[0]
    distance = int(token[1])
    current_position += distance
    if current_position >= len(neighborhood):
        current_position = 0
    if neighborhood[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        neighborhood[current_position] -= 2
        if neighborhood[current_position] == 0:
            print(f"Place {current_position} has Valentine's day.")
    token = input()

unsuccessful_houses = 0
successful = True
for house in neighborhood:
    if house > 0:
        unsuccessful_houses += 1
        successful = False

print(f"Cupid's last position was {current_position}.")
if successful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {unsuccessful_houses} places.")