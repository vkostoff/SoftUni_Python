cards_list = input().split()
shuffles = int(input())

half_size = len(cards_list) // 2

for i in range(shuffles):
    left_side = cards_list[0: half_size]
    right_side = cards_list[half_size:]

    new_list = []

    for j in range(len(left_side)):
        new_list.append(left_side[j])
        new_list.append(right_side[j])

    cards_list = new_list

print(cards_list)