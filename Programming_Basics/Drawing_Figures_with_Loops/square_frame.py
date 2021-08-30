side_a = int(input())

side_b = side_a

print("+ " + ((side_a - 2) * "- ") + "+ ")

for i in range(1, side_a - 1):
    print("| " + ((side_a - 2) * "- ") + "| ")
    
print("+ " + ((side_a - 2) * "- ") + "+ ")
