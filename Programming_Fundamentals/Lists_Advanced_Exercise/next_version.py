new_list = [int(x) for x in input().split(".")]
new_list[2] += 1
if new_list[2] > 9:
    new_list[2] = 0
    new_list[1] += 1
if new_list[1] > 9:
    new_list[1] = 0
    new_list[0] += 1
if new_list[0] > 9:
    new_list[0] = 0
    new_list[2] += 1
new_string = [str(y) for y in new_list]
print(".".join(new_string))