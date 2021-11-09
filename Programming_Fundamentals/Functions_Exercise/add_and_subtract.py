first_number = int(input())
second_number = int(input())
third_number = int(input())


def add_and_subtract(a, b, c):
    def sum_numbers():
        return a + b

    def subtract():
        return sum_numbers() - c
    return subtract()


print(add_and_subtract(first_number, second_number, third_number))