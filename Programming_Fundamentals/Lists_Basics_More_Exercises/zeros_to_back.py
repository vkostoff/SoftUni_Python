original_list = list(input().split(", "))

new_list = []
zero_list = []

for number in original_list:
    
    if not int(number) == 0:
        new_list.append(int(number))
        
    else:
        zero_list.append(int(number))
        
new_list.extend(zero_list)

print(new_list)
