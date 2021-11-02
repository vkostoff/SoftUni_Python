number = int(input())

for n in range(1, number + 1):
    digits_sum = 0
    digits = n
    
    while digits > 0:
        digits_sum += digits % 10
        digits = int(digits / 10)
        
    if (digits_sum == 5) or (digits_sum == 7) or (digits_sum == 11):
        print(f"{n} -> True")
        
    else:
        print(f"{n} -> False")
