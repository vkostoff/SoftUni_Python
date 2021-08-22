import sys

numbers = int(input())

max_number = -sys.maxsize
number_sum = 0

for number in range(numbers):
    current_number = int(input())
    
    if current_number > max_number:
        max_number = current_number
        
    number_sum += current_number
    
if max_number == number_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
    
else:
    difference = abs(max_number - (number_sum - max_number))
    print("No")
    print(f"Diff = {difference}")
