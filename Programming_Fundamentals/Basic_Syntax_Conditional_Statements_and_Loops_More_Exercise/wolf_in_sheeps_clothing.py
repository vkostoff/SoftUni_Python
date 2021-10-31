animals = input()

counter = 0
current_animal = ""
animals = animals.replace(",", "")
animals = animals.split()

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
    
else:
    for i in range(len(animals)-1, -1, -1):
        
        if animals[i] == "sheep":
            counter += 1
            current_animal = animals[i]
        elif animals[i] == "wolf":
            
            print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!" )
            break
