courses = {}

command = input()
while not command == "end":
    command = command.split(" : ")
    if command[0] not in courses:
        courses[command[0]] = []
    courses[command[0]].append(command[1])

    command = input()

ordered_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for k, v in ordered_courses.items():
    print(f"{k}: {len(v)}")

    for i in sorted(v):
        print(f"-- {i}")
