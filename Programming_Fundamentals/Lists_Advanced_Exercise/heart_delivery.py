neighborhood = [int(x) for x in input().split("@")]
step = 0
success = False
command = input()

while not command == "Love!":
    token = command.split(" ")
    step += int(token[1])
    
    if step >= len(neighborhood):
        step = 0
        
    if neighborhood[step] == 0:
        print(f"Place {step} already had Valentine's day.")
        
    else:
        neighborhood[step] -= 2
        
        if neighborhood[step] == 0:
            print(f"Place {step} has Valentine's day.")
            
    command = input()
    
print(f"Cupid's last position was {step}.")

successful = 0
fails = 0

for i in neighborhood:
    successful += i
    
    if i > 0:
        fails += 1
        
if successful == 0:
    success = True
    
if success:
    print("Mission was successful.")
    
else:
    print(f"Cupid has failed {fails} places.")
