message = input()
emoticons = []

for i in range(len(message)):
    if message[i] == ":" and not message[i + 1] == " ":
        emoticons.append(message[i] + message[i + 1])

for j in emoticons:
    print(j)