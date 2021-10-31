word = input()
new_list = []

for i in range(len(word)):
    if word[i].isupper():
        new_list.append(i)
        
print(new_list)
