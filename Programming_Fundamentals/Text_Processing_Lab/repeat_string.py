sequence = input().split()
new_string = ""

for i in sequence:
    new_string += (i * len(i))

print(new_string)