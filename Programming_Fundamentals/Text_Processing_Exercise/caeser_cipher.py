initial_message = input()
new_message = ""

for i in initial_message:
    new_message += chr(ord(i) + 3)

print(new_message)
