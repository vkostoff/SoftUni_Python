rooms = int(input())

chairs = 0
visitors = 0

for i in range(1, rooms + 1):
    temporary_list = input().split(" ")
    chairs += len(temporary_list[0])
    visitors += int(temporary_list[1])
    
    if int(temporary_list[1]) > len(temporary_list[0]):
        chairs_needed = int(temporary_list[1]) - len(temporary_list[0])
        print(f"{chairs_needed} more chairs needed in room {i}")

if chairs >= visitors:
    chairs_left = chairs - visitors
    print(f"Game On, {chairs_left} free chairs left")
