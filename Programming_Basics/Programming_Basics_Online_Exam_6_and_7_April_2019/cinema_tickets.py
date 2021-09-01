all_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
command = input()
while command != "Finish":
    movie = command
    free_seats = int(input())
    counter = 0
    command_two = input()
    while command_two != "End":
        ticket_type = command_two
        all_tickets += 1
        counter += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        if counter == free_seats:
            break
        command_two = input()
    percentage_full = counter * 100 / free_seats
    print(f"{movie} - {percentage_full:.2f}% full.")
    command = input()
students_percentage = student_tickets * 100 / all_tickets
standard_percentage = standard_tickets * 100 / all_tickets
kids_percentage = kids_tickets * 100 / all_tickets
print(f"Total tickets: {all_tickets}")
print(f"{students_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")
