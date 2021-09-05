from math import ceil
wall_height = int(input())
wall_width = int(input())
non_painted_percentage = int(input())
to_be_painted = 4 * (wall_height * wall_width)
not_to_be_painted = to_be_painted * (non_painted_percentage / 100)
total_to_be_painted = to_be_painted - not_to_be_painted
painted = 0
paint_enough = False
command = input()
while command != "Tired!":
    litters_paint = int(command)
    painted += litters_paint
    if painted >= ceil(total_to_be_painted):
        paint_enough = True
        break
    command = input()
if paint_enough:
    if painted - total_to_be_painted == 0:
        print("All walls are painted! Great job, Pesho!")
    else:
        paint_left = painted - total_to_be_painted
        print(f"All walls are painted and you have {int(paint_left)} l paint left!")
else:
    space_left = total_to_be_painted - painted
    print(f"{ceil(space_left)} quadratic m left." )