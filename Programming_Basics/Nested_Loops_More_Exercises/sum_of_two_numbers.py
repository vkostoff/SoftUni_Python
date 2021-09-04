beginning = int(input())
end = int(input())
magic_number = int(input())
combination = 0
magic_number_found = False
for first in range(beginning, end + 1):
    for second in range(beginning, end + 1):
        combination += 1
        if first + second == magic_number:
            magic_number_found = True
            break
    if magic_number_found:
        break
if magic_number_found:
    print(f"Combination N:{combination} ({first} + {second} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")