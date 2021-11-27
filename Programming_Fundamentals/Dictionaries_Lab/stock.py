array = input().split()

my_dict = {}

for i in range(0, len(array), 2):
    key = array[i]
    value = int(array[i + 1])
    my_dict[key] = value

searched_products = input().split()

for product in searched_products:
    if product in my_dict.keys():
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")