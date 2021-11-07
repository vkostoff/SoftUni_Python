original_list = list(input().split(" "))
filtered_list = []

for n in range(len(original_list)):
    
    if int(original_list[n]) > 0:
        filtered_list.append(-int(original_list[n]))
        
    elif int(original_list[n]) < 0:
        filtered_list.append(abs(int(original_list[n])))
        
    else:
        filtered_list.append(int(original_list[n]))
        
print(filtered_list)
