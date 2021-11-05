fire_list = input().split("#")
water = int(input())

total_fire = 0
effort = 0
put_out_cells = []

print("Cells:")


for fire in fire_list:
    args = fire.split(sep=" = ")
    fire_type = args[0]
    fire_value = int(args[1])
    valid = False

    if water < fire_value:
        continue

    if fire_type == "High":
        if 81 <= fire_value <= 125:
            valid = True
    elif fire_type == "Medium":
        if 51 <= fire_value <= 80:
            valid = True
    elif fire_type == "Low":
        if 1 <= fire_value <= 50:
            valid = True
 