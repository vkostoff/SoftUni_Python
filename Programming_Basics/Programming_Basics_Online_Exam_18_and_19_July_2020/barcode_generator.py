beginning = int(input())
end = int(input())

first_beginning = int(beginning / 1000)
second_beginning = int((beginning / 100) % 10)
third_beginning = int((beginning / 10) % 10)
fourth_beginning = int(beginning % 10)

first_end = int(end / 1000)
second_end = int((end / 100) % 10)
third_end = int((end / 10) % 10)
fourth_end = int(end % 10)

for n1 in range(first_beginning, first_end + 1):
    for n2 in range(second_beginning, second_end + 1):
        for n3 in range(third_beginning, third_end + 1):
            for n4 in range(fourth_beginning, fourth_end + 1):
                if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
                    print(f"{n1}{n2}{n3}{n4}", end=' ')
