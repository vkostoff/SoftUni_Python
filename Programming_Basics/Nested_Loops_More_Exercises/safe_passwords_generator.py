a = int(input())
b = int(input())
max_passwords = int(input())
counter = 0
first = 35
second = 64
fifth = 64
sixth = 35
max_reached = False
for third in range(1, a + 1):
    for fourth in range(1, b + 1):
        print(f"{chr(first)}{chr(second)}{third}{fourth}{chr(fifth)}{chr(sixth)}", end="|")
        first += 1
        second += 1
        fifth += 1
        sixth += 1
        counter += 1

        if first > 55:
            first = 35
        if second > 96:
            second = 64
        if fifth > 96:
            fifth = 64
        if sixth > 55:
            sixth = 35
        if counter >= max_passwords:
            max_reached = True
            break
    if max_reached:
        break
