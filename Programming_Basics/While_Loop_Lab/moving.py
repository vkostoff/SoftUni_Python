place_width = int(input())
place_length = int(input())
place_height = int(input())
place_volume = place_width * place_height * place_length
command = input()
while command != "Done":
    packages_count = int(command)
    if place_volume < packages_count:
        print(f"No more free space! You need {packages_count - place_volume} Cubic meters more.")
        place_volume -= packages_count
        break
    place_volume -= packages_count
    command = input()
if place_volume > 0:
    print(f"{place_volume} Cubic meters left.")
