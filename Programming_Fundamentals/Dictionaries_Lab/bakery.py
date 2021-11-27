array = input().split()

my_dict = {}

for i in range(0, len(array), 2):
    key = array[i]
    value = int(array[i + 1])
    my_dict[key] = value


print(my_dict)