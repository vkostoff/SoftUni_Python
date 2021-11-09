def perfect_number():
    number = int(input())
    new_number = 0
    for i in range(number, 0, -1):
        if number % i == 0:
            new_number += i
    if new_number / 2 == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number())
