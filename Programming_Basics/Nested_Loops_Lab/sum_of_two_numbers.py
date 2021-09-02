start = int(input())
end = int(input())
target_number = int(input())

counter = 0

flag = False

for x in range(start, end + 1):
    
    for y in range(start, end + 1):
        combination = x + y
        counter += 1
        
        if combination == target_number:
            print(f"Combination N:{counter} ({x} + {y} = {target_number})")
            
            flag = True
            
            break
            
    if flag:
        break
        
if not flag:
    print(f"{counter} combinations - neither equals {target_number}")
