numbers = list(input().split(sep=" "))
string = list(input())

found = False
counter = 0
message = ""
temporary_sum = 0

for number in numbers:
    for n in number:
        temporary_sum += int(n)
        found = False
        
    while not found:
        for i in string:
            if counter == temporary_sum:
                if temporary_sum > len(message):
                    message += string[temporary_sum - len(string)]
                    string.pop(temporary_sum - len(string))
                    temporary_sum = 0
                    counter = 0
                    found = True
                    break
                    
                else:
                    message += string[temporary_sum]
                    string.pop(temporary_sum)
                    temporary_sum = 0
                    counter = 0
                    found = True
                    break
                    
            else:
                counter += 1
                
print(message)
