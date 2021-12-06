contest_password_record = {}
submissions = {}
best_result = {}

command = input()
while not command == "end of contests":
    if len(command) == 0:
        exit()
    command = command.split(":")
    contest = command[0]
    password_for_contest = command[1]
    if contest not in contest_password_record:
        contest_password_record[contest] = password_for_contest
    command = input()

command_two = input()
while not command_two == "end of submissions":
    command_two = command_two.split("=>")
    contest = command_two[0]
    password = command_two[1]
    username = command_two[2]
    points = int(command_two[3])
    if contest in contest_password_record:
        if contest_password_record[contest] == password:
            if username not in submissions:
                submissions[username] = {contest: points}
                best_result[username] = points
            elif username in submissions and contest not in submissions[username]:
                submissions[username][contest] = points
                best_result[username] += points
            elif points > submissions[username][contest]:
                submissions[username][contest] = points
                best_result[username] += points
    command_two = input()

sorted_results = dict(sorted(best_result.items(), key=lambda x: -x[1]))

for key, value in sorted_results.items():
    print(f"Best candidate is {key} with total {value} points.")
    break

print("Ranking:")

sorted_submissions = dict(sorted(submissions.items(), key=lambda x: x[0]))

for k, v in sorted_submissions.items():
    print(k)
    sorted_sub = dict(sorted(submissions[k].items(), key=lambda x: -x[1]))
    for i in sorted_sub:
        print(f"#  {i} -> {submissions[k][i]}")