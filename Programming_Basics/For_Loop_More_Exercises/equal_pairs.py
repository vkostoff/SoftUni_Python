pair_number = int(input())

current_sum = 0
difference = 0
max_difference = 0

for number in range(1, pair_number + 1):
    first_number = int(input())
    second_number = int(input())
    
    sum_numbers = first_number + second_number
    
    if number == 1:
        current_sum = sum_numbers
        
    else:
        difference = abs(current_sum - sum_numbers)
        current_sum = sum_numbers
        
    if difference > max_difference:
        max_difference = difference

if difference == 0:
    print(f"Yes, value={current_sum}")
    
else:
    print(f"No, maxdiff={max_difference}")
