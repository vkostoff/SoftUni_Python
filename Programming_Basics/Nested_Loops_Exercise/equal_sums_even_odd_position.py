first_number = int(input())
second_number = int(input())
for n in range(first_number, second_number + 1):
    n_to_str = str(n)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(n_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(n, end=" ")