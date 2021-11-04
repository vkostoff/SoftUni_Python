number = int(input())
word = input()

first_list = []

for n in range(1, number + 1):
    string = input()
    first_list.append(string)
    
print(first_list)

for index in range(len(first_list) - 1, -1, -1):
    if word not in first_list[index]:
        first_list.remove(first_list[index])
        
print(first_list)
