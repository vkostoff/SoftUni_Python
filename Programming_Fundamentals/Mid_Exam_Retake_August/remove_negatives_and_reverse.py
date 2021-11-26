numbers = [int(x) for x in input().split()]
new_list = []
for number in numbers:
    if number >= 0:
        new_list.append(number)
if len(new_list) > 0:
    print(*list(reversed(new_list)))
else:
    print("empty")