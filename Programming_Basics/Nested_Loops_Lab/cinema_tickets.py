movie = input()
student_counter = 0
standard_counter = 0
kids_counter = 0
while movie != "Finish":
    free_space = int(input())
    current_people = 0
    for t in range(0, free_space):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kids_counter += 1
        current_people += 1
    percentage = current_people / free_space * 100
    print(f'{movie} - {percentage:.2f}% full.')
    movie = input()
total_tickets = kids_counter + student_counter + standard_counter
student_percent = student_counter / total_tickets * 100
standard_percent = standard_counter / total_tickets * 100
kids_percent = kids_counter / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f'{student_percent:.2f}% student tickets.')
print(f'{standard_percent:.2f}% standard tickets.')
print(f'{kids_percent:.2f}% kids tickets.')
