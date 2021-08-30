number = int(input())

upper_row_stars = (2 * number) * "*"
upper_row_intervals = number * " "
slashes = ((number * 2) - 2) * "/"
vertical_lines = number * "|"
middle_row = (number-1) / 2

print(upper_row_stars + upper_row_intervals + upper_row_stars)

for i in range(1, number - 1):
    
    if i == middle_row and number % 2 == 1:
        print("*" + slashes + "*" + vertical_lines + "*" + slashes + "*")
        
    elif number % 2 == 0 and i == int(middle_row):
        print("*" + slashes + "*" + vertical_lines + "*" + slashes + "*")
        
    else:
        print("*" + slashes + "*" + upper_row_intervals + "*" + slashes + "*")
        
print(upper_row_stars + upper_row_intervals + upper_row_stars)
