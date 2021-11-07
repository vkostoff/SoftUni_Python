numbers = input().split(" ")
number_list = []
num = ""
for n in numbers:
    number_list.append(n)
number_list.sort(reverse=True)
for i in number_list:
    num += i
print(int(num))