import sys


def max_even(int_list):
    max_even_number = -sys.maxsize
    max_even_index = "0"
    for i in range(len(int_list)):
        if int_list[i] % 2 == 0 and int_list[i] >= max_even_number:
            max_even_number = int_list[i]
            max_even_index = i
    if max_even_index == "0":
        max_even_index = "No matches"
    return max_even_index


def min_even(int_list):
    min_even_number = sys.maxsize
    min_even_index = "0"
    for i in range(len(int_list)):
        if int_list[i] % 2 == 0 and int_list[i] <= min_even_number:
            min_even_number = int_list[i]
            min_even_index = i
    if min_even_index == "0":
        min_even_index = "No matches"
    return min_even_index


def max_odd(int_list):
    max_odd_number = -sys.maxsize
    max_odd_index = "0"
    for i in range(len(int_list)):
        if not int(int_list[i]) % 2 == 0 and int(int_list[i]) >= max_odd_number:
            max_odd_number = int_list[i]
            max_odd_index = i
    if max_odd_index == "0":
        max_odd_index = "No matches"
    return max_odd_index


def min_odd(int_list):
    min_odd_number = sys.maxsize
    min_odd_index = "0"
    for i in range(len(int_list)):
        if not int(int_list[i]) % 2 == 0 and int(int_list[i]) <= min_odd_number:
            min_odd_number = int_list[i]
            min_odd_index = i
    if min_odd_index == "0":
        min_odd_index = "No matches"
    return min_odd_index


def first_even(int_list, order):
    if int(order[1]) > len(int_list):
        return "Invalid count"
    else:
        new_list = []
        for i in int_list:
            if i % 2 == 0:
                new_list.append(i)
                if len(new_list) == int(order[1]):
                    break
        return new_list


def first_odd(int_list, order):
    if int(order[1]) > len(int_list):
        return "Invalid count"
    else:
        new_list = []
        for i in int_list:
            if not i % 2 == 0:
                new_list.append(i)
                if len(new_list) == int(order[1]):
                    break
        return new_list


def last_even(int_list, order):
    if int(order[1]) > len(int_list):
        return "Invalid count"
    else:
        new_list = []
        for i in int_list:
            if i % 2 == 0:
                new_list.append(i)
        return new_list[-int(order[1]):]


def last_odd(int_list, order):
    if int(order[1]) > len(int_list):
        return "Invalid count"
    else:
        new_list = []
        for i in int_list:
            if not i % 2 == 0:
                new_list.append(i)
        return new_list[-int(order[1]):]


integers_list = [int(x) for x in input().split(" ")]
new_command = input()
while not new_command == "end":
    command = new_command.split(" ")
    if command[0] == "exchange":
        if int(command[1]) >= len(integers_list) or int(command[1]) < 0:
            print("Invalid index")
        else:
            integers_list = integers_list[int(command[1]) + 1:] + integers_list[0:int(command[1]) + 1]
    elif command[0] == "max":
        if command[1] == "even":
            print(max_even(integers_list))
        elif command[1] == "odd":
            print(max_odd(integers_list))
    elif command[0] == "min":
        if command[1] == "even":
            print(min_even(integers_list))
        elif command[1] == "odd":
            print(min_odd(integers_list))
    elif command[0] == "first":
        if command[2] == "even":
            print(first_even(integers_list, command))
        elif command[2] == "odd":
            print(first_odd(integers_list, command))
    elif command[0] == "last":
        if command[2] == "even":
            print(last_even(integers_list, command))
        elif command[2] == "odd":
            print(last_odd(integers_list, command))
    new_command = input()
print(integers_list)
