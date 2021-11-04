number = int(input())

list_of_integers = []
filtered = []

for n in range(1, number + 1):
    integer = int(input())
    list_of_integers.append(integer)
    
category = input()

if category == "even":
    for i in range(len(list_of_integers)):
        if list_of_integers[i] % 2 == 0:
            filtered.append(list_of_integers[i])
            
elif category == "odd":
    for i in range(len(list_of_integers)):
        if not list_of_integers[i] % 2 == 0:
            filtered.append(list_of_integers[i])
            
elif category == "negative":
    for i in range(len(list_of_integers)):
        if list_of_integers[i] < 0:
            filtered.append(list_of_integers[i])
            
elif category == "positive":
    for i in range(len(list_of_integers)):
        if list_of_integers[i] >= 0:
            filtered.append(list_of_integers[i])
            
print(filtered)
