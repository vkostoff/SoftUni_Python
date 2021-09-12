wall_height = int(input())
wall_width = int(input())
not_to_be_painted = int(input())

to_be_painted = (wall_width * wall_height) * 4
not_to_be_painted_percentage = to_be_painted * (not_to_be_painted / 100)
total_to_be_painted = to_be_painted - not_to_be_painted_percentage

painted = 0

all_pained = False

command = input()

while command != "Tired!":
    liters_paint = int(command)
    
    painted += liters_paint
    
    if painted >= total_to_be_painted:
        all_pained = True
        break
        
    command = input()
    
if all_pained and painted - total_to_be_painted == 0:
    print("All walls are painted! Great job, Pesho!" )
    
elif all_pained and painted - total_to_be_painted > 0:
    paint_left = painted - total_to_be_painted
    print(f"All walls are painted and you have {int(paint_left)} l paint left!")
    
else:
    paint_needed = total_to_be_painted - painted
    print(f"{int(paint_needed)} quadratic m left." )
