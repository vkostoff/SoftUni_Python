from math import pi

figure_type = input()

if figure_type == "square":
    side = float(input())
    square_area = side * side
    print(f"{square_area:.3f}")

elif figure_type == "rectangle":
    side_one = float(input())
    side_two = float(input())
    rectangle_area = side_one * side_two
    print(f"{rectangle_area:.3f}")

elif figure_type == "circle":
    radius = float(input())
    circle_area = (radius * radius) * pi
    print(f"{circle_area:.3f}")

elif figure_type == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    triangle_area = (triangle_height * triangle_side) / 2
    print(f"{triangle_area:.3f}")
