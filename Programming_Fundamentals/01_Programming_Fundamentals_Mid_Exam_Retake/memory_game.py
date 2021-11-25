elements_sequence = [x for x in input().split()]
moves = 0
command = input()
while not command == "end":
    pair = [int(x) for x in command.split()]
    i1 = pair[0]
    i2 = pair[1]
    if i1 == i2 or i1 not in range(len(elements_sequence)) or i2 not in range(len(elements_sequence)):
        moves += 1
        middle = len(elements_sequence) // 2
        elements_sequence.insert(middle, f"-{moves}a")
        elements_sequence.insert(middle, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements_sequence[i1] == elements_sequence[i2]:
        element = elements_sequence[i1]
        elements_sequence.remove(element), elements_sequence.remove(element)
        moves += 1
        print(f"Congrats! You have found matching elements - {element}!")
    elif not elements_sequence[i1] == elements_sequence[i2]:
        print("Try again!")
    if len(elements_sequence) == 0:
        print(f"You have won in {moves} turns!")
        break
    command = input()
if len(elements_sequence) > 0:
    print("Sorry you lose :(""\n"f"{' '.join(elements_sequence)}")