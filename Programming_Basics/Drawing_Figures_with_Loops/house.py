number = int(input())
roof_rows = (number + 1) // 2
roof_intervals = 0
roof_stars = 0
if number % 2 == 0:
    roof_intervals = number // 2 - 1
    roof_stars = 2
    print((roof_intervals * "-") + (roof_stars * "*") + (roof_intervals * "-"))
    for i in range(1, roof_rows):
        roof_stars += 2
        roof_intervals -= 1
        print((roof_intervals * "-") + (roof_stars * "*") + (roof_intervals * "-"))
elif number % 2 == 1:
    roof_intervals = number // 2
    roof_stars = 1
    print((roof_intervals * "-") + (roof_stars * "*") + (roof_intervals * "-"))
    for i in range(1, roof_rows):
        roof_stars += 2
        roof_intervals -= 1
        print((roof_intervals * "-") + (roof_stars * "*") + (roof_intervals * "-"))

fundament_rows = number // 2
fundament_stars = number - 2
print("|" + (fundament_stars * "*") + "|")
for j in range(1, fundament_rows):
    print("|" + (fundament_stars * "*") + "|")