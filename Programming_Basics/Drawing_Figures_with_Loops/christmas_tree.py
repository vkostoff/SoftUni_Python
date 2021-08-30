number = int(input())

free_space = number
star = 0

print(free_space * " " + star * "*" + " | " + star * "*" + free_space * " ")

for i in range(1, number + 1):
    free_space -= 1
    star += 1
    
    print(free_space * " " + star * "*" + " | " + star * "*" + free_space * " ")
