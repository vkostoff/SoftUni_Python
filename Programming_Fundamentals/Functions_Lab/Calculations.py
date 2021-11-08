action = input()
number_one = int(input())
number_two = int(input())


def calculate(a, b, operator):
    result = None
    if action == "multiply":
        result = number_one * number_two
    elif action == "divide":
        result = number_one / number_two
    elif action == "add":
        result = number_one + number_two
    elif action == "subtract":
        result = number_one - number_two
    return int(result)


print(calculate(number_one, number_two, action))
