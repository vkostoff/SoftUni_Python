number = int(input())
free_space = number
star = 0
for i in range(1, number + 1):
    free_space -= 1
    star += 1
    print(free_space * " " + star * "* ")
for j in range(number, 1, -1):
    free_space += 1
    star -= 1
    print(free_space * " " + star * "* ")

