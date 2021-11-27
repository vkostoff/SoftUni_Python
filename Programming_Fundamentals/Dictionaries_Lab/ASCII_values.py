characters_list = input().split(", ")

dictionary = {}

for characters in characters_list:
    dictionary[characters] = ord(characters)

print(dictionary)