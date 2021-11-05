factor = int(input())
count = int(input())
new_list = []

for n in range(1, count + 1):
    new_list.append(n * factor)
    
print(new_list)
