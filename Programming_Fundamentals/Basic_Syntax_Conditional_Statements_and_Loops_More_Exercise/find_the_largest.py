number = list(input())
number.sort(reverse=True)

for k in range(len(number)):
    print(number[k], end="")
