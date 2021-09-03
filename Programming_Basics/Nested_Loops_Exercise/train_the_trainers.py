number_of_jury = int(input())
final_degree = 0
number_of_presentations = 0
command = input()
while command != "Finish":
    presentation_name = command
    current_presentation_grade = 0
    for jury in range(1, number_of_jury + 1):
        current_jury_grade = float(input())
        current_presentation_grade += current_jury_grade
        final_degree += current_jury_grade
        number_of_presentations += 1
    presentation_average_grade = current_presentation_grade / number_of_jury
    print(f"{presentation_name} - {presentation_average_grade:.2f}.")
    command = input()
average_grade = final_degree / number_of_presentations
print(f"Student's final assessment is {average_grade:.2f}.")