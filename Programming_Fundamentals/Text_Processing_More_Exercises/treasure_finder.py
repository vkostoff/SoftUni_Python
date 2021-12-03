key = [int(x) for x in input().split()]

command = input()
while not command == "find":
    material = ""
    coordinates = ""
    string_sequence = [x for x in command]
    n = 0
    
    for i in range(len(string_sequence)):
        string_sequence[i] = chr(ord(string_sequence[i]) - key[n])
        if n == len(key) - 1:
            n = 0
            
        else:
            n += 1
            
    material_found = False
    
    for j in range(len(string_sequence)):
        if string_sequence[j] == "&":
            for k in range(j+1, len(string_sequence)):
                if string_sequence[k] == "&":
                    material_found = True
                    break
                    
                else:
                    material += string_sequence[k]
                    
            if material_found:
                break
                
    coordinates_found = False
    
    for y in range(len(string_sequence)):
        if string_sequence[y] == "<":
            for m in range(y + 1, len(string_sequence)):
                if string_sequence[m] == ">":
                    coordinates_found = True
                    break
                    
                else:
                    coordinates += string_sequence[m]
                    
            if material_found:
                break
                
    if material_found and coordinates_found:
        print(f"Found {material} at {coordinates}")
        
    command = input()
