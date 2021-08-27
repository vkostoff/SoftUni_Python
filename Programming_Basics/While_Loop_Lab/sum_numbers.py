target_number = int(input())
current_sum = 0

while current_sum < target_number:
    new_number = int(input())
    current_sum += new_number

print(current_sum)