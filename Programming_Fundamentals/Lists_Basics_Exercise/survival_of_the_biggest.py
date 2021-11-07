numbers_list = list(input().split(sep=" "))
numbers_list = [int(x) for x in numbers_list]
to_be_removed = int(input())

new_list = sorted(numbers_list)[to_be_removed:]
the_list = []

for numbers in numbers_list:
    if numbers in new_list:
        the_list.append(numbers)
        
print(*the_list, sep=", ")
