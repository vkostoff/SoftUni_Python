lines = int(input())

capacity = 255
filled = 0

for i in range(1, lines + 1):
    fill = int(input())
    
    if (filled + fill) > capacity:
        print("Insufficient capacity!")
        
    else:
        filled += fill
        
print(filled)
