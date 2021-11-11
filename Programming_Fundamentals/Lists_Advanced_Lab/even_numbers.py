list_of_numbers = [int(x) for x in input().split(", ")]
new_list = []
for i in range(len(list_of_numbers)):
    if list_of_numbers[i] % 2 == 0:
        new_list.append(i)
print(new_list)