strings = input().split()
new_string = ""

total_sum = 0

if len(strings[0]) > len(strings[1]):
    new_string = strings[0][len(strings[1])::]
    strings[0] = strings[0][:len(strings[1]):]
    print(sum([ord(strings[0][x]) * ord(strings[1][x]) for x in range(len(strings[0]))]) + ord(new_string))
elif len(strings[1]) > len(strings[0]):
    new_string = strings[1][len(strings[0])::]
    strings[1] = strings[1][:len(strings[0]):]
    new_string = sum([ord(x) for x in new_string])
    print(sum([ord(strings[0][x]) * ord(strings[1][x]) for x in range(len(strings[0]))]) + new_string)
else:
    print(sum([ord(strings[0][x]) * ord(strings[1][x]) for x in range(len(strings[0]))]))