number = int(input())

positive_list = []
negative_list = []
positives = 0
negatives = 0

for n in range(1, number + 1):
    integer = int(input())
    
    if integer >= 0:
        positive_list.append(integer)
        positives += 1
        
    else:
        negative_list.append(integer)
        negatives += integer
        
print(positive_list)
print(negative_list)
print(f"Count of positives: {positives}. Sum of negatives: {negatives}")
