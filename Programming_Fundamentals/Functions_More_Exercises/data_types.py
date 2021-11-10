def data_type(command, string):
    result = ""
    if command == "int":
        result = int(string) * 2
    elif command == "real":
        result = f"{float(string) * 1.5:.2f}"
    elif command == "string":
        result = f"${string}$"
    return result


word = input()
second_word = input()
print(data_type(word, second_word))
