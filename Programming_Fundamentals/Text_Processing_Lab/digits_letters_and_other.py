string = input()

letters = ""
digits = ""
others = ""

for i in string:
    if i.isalpha():
        letters += i
        
    elif i.isdigit():
        digits += i
        
    else:
        others += i

print(digits)
print(letters)
print(others)
