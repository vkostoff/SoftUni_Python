m = int(input())

counter = 0

number_found = False

first = 0
second = 0
third = 0
fourth = 0

for a in range(1, 10):
    
    for b in range(1, 10):
        
        for c in range(1, 10):
            
            for d in range(1, 10):
                
                if a < b and c > d:
                    
                    if (a * b) + (c * d) == m:
                        print(f"{a}{b}{c}{d}", end=" ")
                        
                        counter += 1
                        
                        if counter == 4:
                            number_found = True
                            first = a
                            second = b
                            third = c
                            fourth = d
                            
if number_found:
    print()
    print(f"Password: {first}{second}{third}{fourth}")
    
else:
    print()
    print("No!")
