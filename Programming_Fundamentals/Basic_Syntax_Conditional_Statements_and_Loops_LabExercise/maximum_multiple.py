divisor = int(input())
bound = int(input())
for number in range(bound, 1, -1):
    if number % divisor == 0:
        print(number)
        break