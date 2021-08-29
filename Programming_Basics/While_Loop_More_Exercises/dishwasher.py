detergent_bottles = int(input())
detergent_mililiters = detergent_bottles * 750
detergent_needed = 0
counter = 1
clean_dishes = 0
clean_pots = 0
detergent_finished = False
command = input()
while command != "End":
    vessels_count = int(command)
    if counter % 3 == 0:
        clean_pots += vessels_count
        detergent_mililiters -= vessels_count * 15
    else:
        clean_dishes += vessels_count
        detergent_mililiters -= vessels_count * 5
    if detergent_mililiters < 0:
        detergent_finished = True
        break
    counter += 1
    command = input()

if detergent_finished:
    print(f"Not enough detergent, {abs(detergent_mililiters)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {detergent_mililiters} ml.")
