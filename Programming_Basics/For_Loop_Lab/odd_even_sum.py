n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    number = int(input())
    
    if i % 2 == 0:
        even_sum += number
        
    else:
        odd_sum += number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
    
else:
    difference = odd_sum - even_sum
    print("No")
    print(f"Diff = {abs(difference)}")
