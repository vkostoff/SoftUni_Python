lines = int(input())

for line in range(lines):
    string = input()
    name = ""
    age = ""
    
    for i in range(len(string)):
        if string[i] == "@":
            for j in range(i+1, len(string)):
                if not string[j] == "|":
                    name += string[j]
                    
                else:
                    break
                    
    for i in range(len(string)):
        if string[i] == "#":
            for j in range(i+1, len(string)):
                if not string[j] == "*":
                    age += string[j]
                    
                else:
                    break
                    
    print(f"{name} is {age} years old.")
