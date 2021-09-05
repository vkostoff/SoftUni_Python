upper_first = int(input())
upper_second = int(input())
upper_third = int(input())

for first in range(1, upper_first + 1):
    
    for second in range(1, upper_second + 1):
        
        for third in range(1, upper_third + 1):
            
            if first % 2 == 0 and third % 2 == 0:
                
                if second == 2 or second == 3 or second == 5 or second == 7:
                    print(f"{first} {second} {third}")
