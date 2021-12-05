results = {}
submissions = {}

result = input()
while not result == "exam finished":
    if len(result) == 0:
        break
    result = result.split("-")
    if result[1] == "banned":
        del results[result[0]]
        result = input()
        continue
    student = result[0]
    path = result[1]
    score = result[2]
    if path not in submissions:
        submissions[path] = []
    submissions[path].append(student)
    if student not in results:
        results[student] = int(score)
    elif student in results:
        if int(score) > results[student]:
            results[student] = int(score)
    result = input()

sorted_results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
sorted_submissions = dict(sorted(submissions.items(), key=lambda x: (-len(x[1]), x[0])))

if not len(result) == 0 and not len(submissions) == 0:
    print("Results:")
    for k, v in sorted_results.items():
        print(f"{k} | {v}")
    print("Submissions:")
    for k, v in sorted_submissions.items():
        print(f"{k} - {len(v)}")
