ball_count = int(input())
color = ""

total_points = 0
red_points = 0
orange_points = 0
yellow_points = 0
white_points = 0
black_points = 0
other_points = 0

i = 1
while i <= ball_count:
    i += 1
    color = input()

    if color == "red":
        total_points += 5
        red_points += 1
    elif color == "orange":
        total_points += 10
        orange_points += 1
    elif color == "yellow":
        total_points += 15
        yellow_points += 1
    elif color == "white":
        total_points += 20
        white_points += 1
    elif color == "black":
        total_points //= 2
        black_points += 1
    elif color != "red" and color != "orange" and color != "yellow" and color != "white" and color != "black":
        total_points = total_points
        other_points += 1

print(f"Total points: {total_points}")
print(f"Points from red balls: {red_points}")
print(f"Points from orange balls: {orange_points}")
print(f"Points from yellow balls: {yellow_points}")
print(f"Points from white balls: {white_points}")
print(f"Other colors picked: {other_points}")
print(f"Divides from black balls: {black_points}")

