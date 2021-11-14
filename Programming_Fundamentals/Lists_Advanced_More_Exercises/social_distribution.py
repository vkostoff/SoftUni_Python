population = [int(x) for x in input().split(", ")]
min_wealth = int(input())
step = 1
for i in range(len(population)):
    if population[i] < min_wealth:
        to_add = min_wealth - population[i]
        for k in range(len(population)-1, -1, -1):
            if population[k] >= min_wealth + to_add:
                if population[k] >= sorted(population)[-1]:
                    population[k] -= to_add
                    population[i] += to_add
                    break
completed = True
for j in population:
    if j < min_wealth:
        completed = False
        break
if completed is False:
    print("No equal distribution possible")
else:
    print(population)