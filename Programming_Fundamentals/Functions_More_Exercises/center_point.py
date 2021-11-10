from math import floor


def calculate_coordinates(a, b):
    result = abs(a) + abs(b)
    return floor(result)


first = float(input())
second = float(input())
third = float(input())
fourth = float(input())

point_one = calculate_coordinates(first, second)
point_two = calculate_coordinates(third, fourth)

if point_one >= point_two:
    print(f"({floor(third)}, {floor(fourth)})")
else:
    print(f"({floor(first)}, {floor(second)})")
