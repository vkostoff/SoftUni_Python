first_list = input().split(", ")
second_list = "".join(input().split(", "))
new_list = [x for x in first_list if x in second_list]
print(new_list)