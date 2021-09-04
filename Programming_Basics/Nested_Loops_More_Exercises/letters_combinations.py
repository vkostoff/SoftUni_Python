first = input()
second = input()
third = input()

counter = 0

for f in range(ord(first), ord(second) + 1):
    
    if f == ord(third):
        continue
        
    for t in range(ord(first), ord(second) + 1):
        
        if t == ord(third):
            continue
            
        for s in range(ord(first), ord(second) + 1):
            
            if s == ord(third):
                continue
                
            print(f"{chr(f)}{chr(t)}{chr(s)}", end=" ")
            
            counter += 1
            
print(counter)
