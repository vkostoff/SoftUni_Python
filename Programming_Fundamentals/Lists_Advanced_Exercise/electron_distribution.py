number_electrons = int(input())
new_list = []
n = 1

while number_electrons > 0:
    if number_electrons >= 2 * (n ** 2):
        number_electrons -= 2 * (n ** 2)
        new_list.append(2 * (n ** 2))
        
    else:
        new_list.append(number_electrons)
        number_electrons = 0
        
    n += 1
print(new_list)
