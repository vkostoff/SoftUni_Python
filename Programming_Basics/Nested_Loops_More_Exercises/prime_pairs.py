first_beginning = int(input())
second_beginning = int(input())
first_difference = int(input())
second_difference = int(input())
for first in range(first_beginning, (first_beginning + first_difference) + 1):
    for second in range(second_beginning, (second_beginning + second_difference) + 1):
        if first % 2 != 0 and second % 2 != 0 and first % 3 != 0 and second % 3 != 0\
                and first % 5 != 0 and second % 5 != 0 and first % 7 != 0 and second % 7 != 0:
            print(f"{first}{second}")