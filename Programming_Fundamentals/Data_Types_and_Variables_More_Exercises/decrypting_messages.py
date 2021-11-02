key = int(input())
n = int(input())
message = ""
for i in range(1, n + 1):
    letter = input()
    message += chr(ord(letter) + key)
print(message)