initial_list = input().split("|")
new_list = []
new_new_list = []

for i in initial_list[::-1]:
    i = i.split(" ")
    new_list.append(i)
    
for j in new_list:
    for k in j:
        if not k == " ":
            new_new_list.append(k)
            
final_list = []

for z in new_new_list:
    if not z == "":
        final_list.append(z)

print(" ".join(final_list))
