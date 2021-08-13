x = float(input())
y = float(input())
h = float(input())

front_area = (x * x) - 2.4
back_area = x * x
side_area = 2 * ((x * y) - (1.5 * 1.5))
green_paint = (front_area + back_area + side_area) / 3.4

side_roof = 2 * (x * y)
front_back_roof = ((x * h) / 2) * 2
red_paint = (side_roof + front_back_roof) / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
