ban_list = input().split(", ")
text = input()

for i in ban_list:
    if i in text:
        text = text.replace(i, len(i) * "*")

print(text)