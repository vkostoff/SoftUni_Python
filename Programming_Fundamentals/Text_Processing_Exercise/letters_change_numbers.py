def letter_position(let):
    position = ord(let.lower()) - 96
    return position


sequence = input().split()

number = ""

result = 0
final_result = 0

for word in sequence:
    for symbol in word:
        if symbol.isdigit():
            number += symbol
            
    if word[0].isupper():
        result = int(number) / letter_position(word[0])
        
    elif word[0].islower():
        result = int(number) * letter_position(word[0])
        
    if word[-1].isupper():
        result -= letter_position(word[-1])
        
    elif word[-1].islower():
        result += letter_position(word[-1])
        
    final_result += result
    result = 0
    number = ""

print(f"{final_result:.2f}")
