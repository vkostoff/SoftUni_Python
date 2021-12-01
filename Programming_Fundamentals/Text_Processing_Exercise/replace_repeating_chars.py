string = input()
new_string = ""

last_char = ""

for i in string:
    if not i == last_char:
        new_string += i
        last_char = i

print(new_string)