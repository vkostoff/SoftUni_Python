students = {}

command = input()
while ":" in command:
    command = command.split(":")
    name = command[0]
    id = command[1]
    course = command[2]
    students[name] = [id, course]
    command = input()

searched_course = ""
for l in command:
    if l == "_":
        l = " "
    searched_course += l

for key, value in students.items():
    if searched_course in value:
        print(f"{key} - {value[0]}")