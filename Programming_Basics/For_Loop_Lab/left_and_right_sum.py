n = int(input())

sum_left = 0
sum_right = 0

for i in range(2 * n):
    number = int(input())
    if i < n:
        sum_left += number
    else:
        sum_right += number

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    difference = sum_left - sum_right
    print(f"No, diff = {abs(difference)}")