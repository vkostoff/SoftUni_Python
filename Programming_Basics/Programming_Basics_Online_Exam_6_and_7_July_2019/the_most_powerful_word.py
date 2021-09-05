best_result = 0
best_word = ""
command = input()
while command != "End of words":
    word = command
    sum_symbols = 0
    sum_word = 0
    for count, value in enumerate(word):
        sum_symbols += ord(value)
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y"\
        or word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
        sum_word = sum_symbols * len(word)
    else:
        sum_word = sum_symbols / len(word)
    if sum_word >= best_result:
        best_result = sum_word
        best_word = word
    command = input()
print(f"The most powerful word is {best_word} - {best_result}")