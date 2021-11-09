char_one = input()
char_two = input()


def chars_in_range(a, b):
    new_string = []
    for i in range(ord(a)+1, ord(b)):
        new_string += chr(i)
    return new_string


print(*chars_in_range(char_one, char_two))