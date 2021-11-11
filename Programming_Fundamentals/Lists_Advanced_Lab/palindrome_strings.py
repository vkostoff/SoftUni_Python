palindrome_list = input().split(" ")
palindrome = input()
new_list = []
count = 0
for i in range(len(palindrome_list)):
    if palindrome in palindrome_list[i]:
        count += 1
    if not palindrome_list[i] == palindrome_list[i][::-1]:
        palindrome_list[i] = "None"
for j in palindrome_list:
    if "None" not in j:
        new_list.append(j)
print(new_list)
print(f"Found palindrome {count} times")
