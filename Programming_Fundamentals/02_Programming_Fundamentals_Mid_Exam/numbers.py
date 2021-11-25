integers = [int(x) for x in input().split()]
integers.sort(reverse=True)
average = sum(integers) / len(integers)
new_list = []

for i in range(len(integers)):
    if integers[i] > average:
        new_list.append(integers[i])
        
        if len(new_list) == 5:
            break
            
if len(new_list) > 0:
    print(*new_list)
    
else:
    print("No")
