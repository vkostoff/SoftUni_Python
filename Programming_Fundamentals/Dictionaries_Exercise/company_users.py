company_users = {}

command = input()
while not command == "End":
    command = command.split(" -> ")
    if command[0] not in company_users:
        company_users[command[0]] = []
    if command[1] not in company_users[command[0]]:
        company_users[command[0]].append(command[1])
    command = input()

ordered_companies = dict(sorted(company_users.items(), key=lambda x: x[0]))

for k, v in ordered_companies.items():
    print(k)
    for i in v:
        print(f"-- {i}")