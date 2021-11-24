array = [int(x) for x in input().split()]
token = input()

while not token == "end":
    token = token.split()
    
    if token[0] == "swap":
        array[int(token[1])], array[int(token[2])] = array[int(token[2])], array[int(token[1])]
        
    elif token[0] == "multiply":
        array[int(token[1])] *= array[int(token[2])]
        
    elif token[0] == "decrease":
        for i in range(len(array)):
            array[i] -= 1
            
    token = input()
    
array = [str(x) for x in array]
print(", ".join(array))
