initial_energy = int(input())
battles_won = 0
won = True
token = input()

while not token == "End of battle":
    distance = int(token)
    
    if distance > initial_energy:
        won = False
        break
        
    initial_energy -= distance
    battles_won += 1
    
    if battles_won % 3 == 0:
        initial_energy += battles_won
        
    token = input()
    
if won:
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
    
else:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
