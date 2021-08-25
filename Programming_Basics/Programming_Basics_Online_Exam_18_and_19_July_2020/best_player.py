i = 0
best_score = 0
best_player = ""
while i != "END":
    name = input()
    if name != "END":
        goals = int(input())
        if goals > best_score:
            best_score = goals
            best_player = name
        if best_score >= 10:
            break
    else:
        break
print(f"{best_player} is the best player!")
if best_score >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")
