dictionary = {}

text = list(input())

for i in text:
    if i == " ":
        continue
    elif i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")