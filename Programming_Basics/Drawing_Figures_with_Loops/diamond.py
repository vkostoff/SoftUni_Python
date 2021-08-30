from math import ceil

n = int(input())

if n == 1:
    print("*")
    
else:
    dashes = (n - 1) // 2
    diamond_mid = n - 2 * dashes - 2
    middle = n % 2
    
    if diamond_mid < 0:
        print((dashes * "-") + "*" + (dashes * "-"))
        
        for i in range(1, n + 1):
            if i == ceil(n / 2):
                break
                
            dashes -= 1
            
            print((dashes * "-") + "*" + (middle * "-") + "*" + (dashes * "-"))
            
            middle += 2
            
        dashes = 1
        middle = n - 4
        
        for j in range((n // 2), 1, -1):
            print((dashes * "-") + "*" + (middle * "-") + "*" + (dashes * "-"))
            
            dashes += 1
            middle -= 2
            
        print((dashes * "-") + "*" + (dashes * "-"))
        
    else:
        print((dashes * "-") + "*" + (diamond_mid * "-") + "*" + (dashes * "-"))
        
        for i in range(1, n + 1):
            if i == ceil(n / 2):
                break
                
            dashes -= 1
            middle += 2
            
            print((dashes * "-") + "*" + (middle * "-") + "*" + (dashes * "-"))
            
        dashes = 1
        middle = n - 4
        
        for j in range((n // 2), 1, -1):
            print((dashes * "-") + "*" + (middle * "-") + "*" + (dashes * "-"))
            
            dashes += 1
            middle -= 2
