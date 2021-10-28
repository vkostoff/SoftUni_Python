word = input()
reversed_word = ""
for symbol in range(len(word) -1, -1, -1):
    reversed_word += word[symbol]
print(reversed_word)