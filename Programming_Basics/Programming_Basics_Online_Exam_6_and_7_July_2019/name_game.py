total_points = 0
best_player = ""
command = input()
while command != "Stop":
    name = command
    points = 0
    for count, value in enumerate(name):
        number = int(input())
        if value == chr(number):
            points += 10
        else:
            points += 2
    if points >= total_points:
        best_player = name
        total_points = points
    command = input()
print(f"The winner is {best_player} with {total_points} points!")