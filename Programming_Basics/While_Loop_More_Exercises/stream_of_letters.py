word = ""
new_word = ""
secret_c = 0
secret_o = 0
secret_n = 0
command = input()
while command != "End":
    if ord(command) not in range(65, 90) and ord(command) not in range(97, 122):
        command = input()
        continue
    if secret_c == 0 and command == "c":
        secret_c += 1
        if secret_n == 1 and secret_o == 1 and secret_c == 1:
            word += " "
            new_word += word
            word = ""
            secret_c = 0
            secret_o = 0
            secret_n = 0
        command = input()
        continue
    elif secret_c == 1 and command == "c":
        word += command
    elif secret_o == 0 and command == "o":
        secret_o += 1
        if secret_n == 1 and secret_o == 1 and secret_c == 1:
            word += " "
            new_word += word
            word = ""
            secret_c = 0
            secret_o = 0
            secret_n = 0
        command = input()
        continue
    elif secret_o == 1 and command == "o":
        word += command
    elif secret_n == 0 and command == "n":
        secret_n += 1
        if secret_n == 1 and secret_o == 1 and secret_c == 1:
            word += " "
            new_word += word
            word = ""
            secret_c = 0
            secret_o = 0
            secret_n = 0
        command = input()
        continue
    elif secret_n == 1 and command == "n":
        word += command
    else:
        word += command
    command = input()
print(new_word)