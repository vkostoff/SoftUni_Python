men = int(input())
women = int(input())
max_tables = int(input())

counter = 0

tables_full = False

for m in range(1, men + 1):
    
    for w in range(1, women + 1):
        counter += 1
        
        if counter > max_tables:
            tables_full = True
            break
            
        print(f"({m} <-> {w})", end=" ")
        
    if tables_full:
        break
