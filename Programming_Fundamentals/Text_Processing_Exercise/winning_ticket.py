tickets = input().split(", ")

for ticket in tickets:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    left_side = ticket[:10:]
    right_side = ticket[10::]
    left = ""
    right = ""
    for i in range(len(left_side)):
        if left_side[i] == "$":
            left += "$"
        elif not left_side[i] == "$" and not len(left) == 0:
            if len(left) < 6:
                left = ""
            else:
                break
    for i in range(len(right_side)):
        if right_side[i] == "$":
            right += "$"
        elif not right_side[i] == "$" and not len(right) == 0:
            if len(right) < 6:
                right = ""
            else:
                break
    for i in range(len(left_side)):
        if left_side[i] == "#":
            left += "#"
        elif not left_side[i] == "#" and not len(left) == 0:
            if len(left) < 6:
                left = ""
            else:
                break
    for i in range(len(right_side)):
        if right_side[i] == "#":
            right += "#"
        elif not right_side[i] == "#" and not len(right) == 0:
            if len(right) < 6:
                right = ""
            else:
                break
    for i in range(len(left_side)):
        if left_side[i] == "@":
            left += "@"
        elif not left_side[i] == "@" and not len(left) == 0:
            if len(left) < 6:
                left = ""
            else:
                break
    for i in range(len(right_side)):
        if right_side[i] == "@":
            right += "@"
        elif not right_side[i] == "@" and not len(right) == 0:
            if len(right) < 6:
                right = ""
            else:
                break
    for i in range(len(left_side)):
        if left_side[i] == "^":
            left += "^"
        elif not left_side[i] == "^" and not len(left) == 0:
            if len(left) < 6:
                left = ""
            else:
                break
    for i in range(len(right_side)):
        if right_side[i] == "^":
            right += "^"
        elif not right_side[i] == "^" and not len(right) == 0:
            if len(right) < 6:
                right = ""
            else:
                break
    if 10 > left.count("$") >= 6 and 10 > right.count("$") >= 6:
        if left.count("$") == right.count("$"):
            print(f'ticket "{ticket}" - {left.count("$")}$')
        elif left.count("$") > right.count("$"):
            print(f'ticket "{ticket}" - {right.count("$")}$')
        elif left.count("$") < right.count("$"):
            print(f'ticket "{ticket}" - {left.count("$")}$')
    elif 10 > left.count("$") >= 6 and right.count("$") == 10:
        print(f'ticket "{ticket}" - {left.count("$")}$')
    elif left.count("$") == 10 and 10 > right.count("$") >= 6:
        print(f'ticket "{ticket}" - {right.count("$")}$')
    elif left.count("$") == 10 and right.count("$") == 10:
        print(f'ticket "{ticket}" - 10$ Jackpot!')
    elif 10 > left.count("@") >= 6 and 10 > right.count("@") >= 6:
        if left.count("@") == right.count("@"):
            print(f'ticket "{ticket}" - {left.count("@")}@')
        elif left.count("@") > right.count("@"):
            print(f'ticket "{ticket}" - {right.count("@")}@')
        elif left.count("@") < right.count("@"):
            print(f'ticket "{ticket}" - {left.count("@")}@')
    elif 10 > left.count("@") >= 6 and right.count("@") == 10:
        print(f'ticket "{ticket}" - {left.count("@")}@')
    elif left.count("@") == 10 and 10 > right.count("@") >= 6:
        print(f'ticket "{ticket}" - {right.count("@")}@')
    elif left.count("@") == 10 and right.count("@") == 10:
        print(f'ticket "{ticket}" - 10@ Jackpot!')
    elif 10 > left.count("#") >= 6 and 10 > right.count("#") >= 6:
        if left.count("#") == right.count("#"):
            print(f'ticket "{ticket}" - {left.count("#")}#')
        elif left.count("#") > right.count("#"):
            print(f'ticket "{ticket}" - {right.count("#")}#')
        elif left.count("#") < right.count("#"):
            print(f'ticket "{ticket}" - {left.count("#")}#')
    elif 10 > left.count("#") >= 6 and right.count("#") == 10:
        print(f'ticket "{ticket}" - {left.count("#")}#')
    elif left.count("#") == 10 and 10 > right.count("#") >= 6:
        print(f'ticket "{ticket}" - {right.count("#")}#')
    elif left.count("#") == 10 and right.count("#") == 10:
        print(f'ticket "{ticket}" - 10# Jackpot!')
    elif 10 > left.count("^") >= 6 and 10 > right.count("^") >= 6:
        if left.count("^") == right.count("^"):
            print(f'ticket "{ticket}" - {left.count("^")}^')
        elif left.count("^") > right.count("^"):
            print(f'ticket "{ticket}" - {right.count("^")}^')
        elif left.count("^") < right.count("^"):
            print(f'ticket "{ticket}" - {left.count("^")}^')
    elif 10 > left.count("^") >= 6 and right.count("^") == 10:
        print(f'ticket "{ticket}" - {left.count("^")}^')
    elif left.count("^") == 10 and 10 > right.count("^") >= 6:
        print(f'ticket "{ticket}" - {right.count("^")}^')
    elif left.count("^") == 10 and right.count("^") == 10:
        print(f'ticket "{ticket}" - 10^ Jackpot!')
    else:
        print(f'ticket "{ticket}" - no match')
