people = int(input())
current_state = [int(x) for x in input().split()]
empty_slots = False

for i in range(len(current_state)):
    if current_state[i] < 4:
        if people >= 4 - current_state[i]:
            people -= 4 - current_state[i]
            current_state[i] += 4 - current_state[i]
            
        else:
            current_state[i] += people
            people = 0
            print("The lift has empty spots!""\n"f"{' '.join([str(x) for x in current_state])}")
            break
            
full = True
for y in current_state:
    if y < 4:
        full = False
        break
        
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!""\n"f"{' '.join([str(x) for x in current_state])}")
    
elif full and people == 0:
    print(' '.join([str(x) for x in current_state]))
