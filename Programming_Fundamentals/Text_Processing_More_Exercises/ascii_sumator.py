first_char = ord(input())
second_char = ord(input())
string = input()

new_chars_list = []

for i in string:
    if first_char < ord(i) < second_char:
        new_chars_list.append(ord(i))

print(sum(new_chars_list))