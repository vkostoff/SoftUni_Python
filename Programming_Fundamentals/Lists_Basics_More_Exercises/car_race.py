numbers_list = [int(x) for x in input().split(" ")]

first_time = 0
second_time = 0

half = len(numbers_list) // 2
first_half = numbers_list[0:half]
second_half = numbers_list[-1:half:-1]

for i in first_half:
    first_time += i
    if i == 0:
        first_time *= 0.8

for i in second_half:
    second_time += i
    if i == 0:
        second_time *= 0.8

if first_time < second_time:
    print(f"The winner is left with total time: {first_time:.1f}")
else:
    print(f"The winner is right with total time: {second_time:.1f}")