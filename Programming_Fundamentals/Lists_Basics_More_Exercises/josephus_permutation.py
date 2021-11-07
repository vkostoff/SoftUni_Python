numbers_list = list(input().split(" "))
step = int(input())
new_list = []
counter = 0
while len(new_list) < len(numbers_list):
    for i in range(0, len(numbers_list)):
        counter += 1
        if numbers_list[i] == 0:
            counter -= 1
            continue
        if counter == step:
            new_list.append(int(numbers_list[i]))
            numbers_list[i] = 0
            counter = 0
print(str(new_list).replace(" ", ""))