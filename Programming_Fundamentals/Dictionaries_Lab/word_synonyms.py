synonyms = {}

number_of_words = int(input()) * 2

pair = []

for n in range(number_of_words):
    word = input()
    pair.append(word)
    if len(pair) == 2:
        if pair[0] not in synonyms:
            synonyms[pair[0]] = []
        synonyms[pair[0]].append(pair[1])
        pair.clear()

for w in synonyms:
    print(f"{w} - {', '.join(synonyms[w])}")