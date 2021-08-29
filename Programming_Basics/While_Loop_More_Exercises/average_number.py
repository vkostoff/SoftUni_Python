initial_number = int(input())
number_sum = 0
for i in range(1, initial_number + 1):
    number = int(input())
    number_sum += number
print(f"{number_sum / initial_number:.2f}")
