painted_eggs_count = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_count = 0
max_color = ""

for eggs in range(1, painted_eggs_count + 1):
    color = input()
    
    if color == "red":
        red += 1
        
        if red > max_count:
            max_count = red
            max_color = "red"
            
    elif color == "orange":
        orange += 1
        
        if orange > max_count:
            max_count = orange
            max_color = "orange"
            
    elif color == "blue":
        blue += 1
        
        if blue > max_count:
            max_count = blue
            max_color = "blue"
            
    elif color == "green":
        green += 1
        
        if green > max_count:
            max_count = green
            max_color = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_count} -> {max_color}")
