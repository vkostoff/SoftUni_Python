voucher = int(input())

tickets = 0
others = 0

command = input()

while command != "End":
    purchase = command
    
    if len(purchase) > 8:
        
        if ord(purchase[0]) + ord(purchase[1]) > voucher:
            break
            
        voucher -= ord(purchase[0]) + ord(purchase[1])
        tickets += 1
        
    else:
        
        if ord(purchase[0]) > voucher:
            break
            
        voucher -= ord(purchase[0])
        others += 1
       
    command = input()
    
print(f"{tickets}")
print(f"{others}")
