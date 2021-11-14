new_list = "".join(input())
taken_string = ""
skipped_string = ""
numbers_list = [int(x) for x in new_list if x.isnumeric()]
non_numbers_list = [x for x in new_list if not x.isnumeric()]
for i in range(len(numbers_list)):
    if i % 2 == 0:
        taken_string += "".join(non_numbers_list[0:numbers_list[i]])
        non_numbers_list = non_numbers_list[numbers_list[i]:]
    else:
        skipped_string += "".join(non_numbers_list[0:numbers_list[i]])
        non_numbers_list = non_numbers_list[numbers_list[i]:]
print(taken_string)