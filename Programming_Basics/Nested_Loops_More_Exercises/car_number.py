beginning = int(input())
end = int(input())

for first in range(beginning, end + 1):
    
    for second in range(beginning, end + 1):
        
        for third in range(beginning, end + 1):
            
            for fourth in range(beginning, end + 1):
                if (first % 2 == 0 and fourth % 2 == 1) or (first % 2 == 1 and fourth % 2 == 0):
                    
                    if first > fourth:
                        
                        if (second + third) % 2 == 0:
                            print(f"{first}{second}{third}{fourth}", end=" ")
