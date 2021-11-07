first_move = input().split(" ")
second_move = input().split(" ")
third_move = input().split(" ")
if first_move[0] == "1" and second_move[1] == "1" and third_move[2] == "1":
    print("First player won")
elif first_move[2] == "1" and second_move[1] == "1" and third_move[0] == "1":
    print("First player won")
elif first_move[0] == "1" and second_move[0] == "1" and third_move[0] == "1":
    print("First player won")
elif first_move[1] == "1" and second_move[1] == "1" and third_move[1] == "1":
    print("First player won")
elif first_move[2] == "1" and second_move[2] == "1" and third_move[2] == "1":
    print("First player won")
elif first_move[0] == "1" and first_move[1] == "1" and first_move[2] == "1":
    print("First player won")
elif second_move[0] == "1" and second_move[1] == "1" and second_move[2] == "1":
    print("First player won")
elif third_move[0] == "1" and third_move[1] == "1" and third_move[2] == "1":
    print("First player won")
elif first_move[0] == "2" and second_move[1] == "2" and third_move[2] == "2":
    print("Second player won")
elif first_move[2] == "2" and second_move[1] == "2" and third_move[0] == "2":
    print("Second player won")
elif first_move[0] == "2" and second_move[0] == "2" and third_move[0] == "2":
    print("Second player won")
elif first_move[1] == "2" and second_move[1] == "2" and third_move[1] == "2":
    print("Second player won")
elif first_move[2] == "2" and second_move[2] == "2" and third_move[2] == "2":
    print("Second player won")
elif first_move[0] == "2" and first_move[1] == "2" and first_move[2] == "2":
    print("Second player won")
elif second_move[0] == "2" and second_move[1] == "2" and second_move[2] == "2":
    print("Second player won")
elif third_move[0] == "2" and third_move[1] == "2" and third_move[2] == "2":
    print("Second player won")
else:
    print("Draw!")