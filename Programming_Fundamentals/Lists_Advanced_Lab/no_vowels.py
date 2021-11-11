string = input()
vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
new_string = [x for x in string if x not in vowels]
print("".join(new_string))