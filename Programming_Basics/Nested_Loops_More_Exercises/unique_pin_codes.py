upper_first = int(input())
upper_second = int(input())
upper_third = int(input())

for first in range(2, upper_first + 1):
    
    if first % 2 != 0:
        continue
        
    for second in range(2, upper_second + 1):
        
        if second == 4 or second == 6 or second > 7:
            continue
            
        for third in range(2, upper_third + 1):
            if third % 2 != 0:
                continue
                
            print(f"{first} {second} {third}", end="")
            print()
