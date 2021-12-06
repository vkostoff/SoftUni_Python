results = {}
individual_stats = {}

command = input()
while not command == "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    
    if contest not in results:
        results[contest] = {}
        
    if username not in results[contest]:
        results[contest][username] = points
        
    elif username in results[contest]:
        if results[contest][username] < points:
            results[contest][username] = points
            
    command = input()

for k, v in results.items():
    for key, value in results[k].items():
        if key not in individual_stats:
            individual_stats[key] = value
            
        else:
            individual_stats[key] += value

for k, v in results.items():
    results[k] = dict(sorted(results[k].items(), key=lambda x: (-x[1], x[0])))

sorted_individual_stats = dict(sorted(individual_stats.items(), key=lambda x: (-x[1], x[0])))

for path, data in results.items():
    print(f"{path}: {len(data)} participants")
    counter = 1
    
    for name, score in data.items():
        print(f"{counter}. {name} <::> {score}")
        counter += 1

print("Individual standings:")

new_counter = 1
for user, total in sorted_individual_stats.items():
    print(f"{new_counter}. {user} -> {total}")
    new_counter += 1
