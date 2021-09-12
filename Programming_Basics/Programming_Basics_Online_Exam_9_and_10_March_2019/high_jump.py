counter = 0
counter_failed = 0
failed = False
desired_height = int(input())
starting_height = desired_height - 30
current_attempt = int(input())
while starting_height <= desired_height:
    attempt = current_attempt
    if attempt > starting_height:
        starting_height += 5
        counter += 1
        counter_failed = 0
        if starting_height > desired_height:
            break
    elif attempt <= starting_height:
        counter_failed += 1
        counter += 1
    if counter_failed == 3:
        failed = True
        break
    current_attempt = int(input())
if failed:
    print(f"Tihomir failed at {starting_height}cm after {counter} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {desired_height}cm after {counter} jumps.")