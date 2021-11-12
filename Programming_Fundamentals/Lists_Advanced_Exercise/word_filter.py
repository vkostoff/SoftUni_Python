list_of_words = [word for word in input().split(" ") if len(word) % 2 == 0]
for string in list_of_words:
    print(string)