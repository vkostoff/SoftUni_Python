n = int(input())
current_symbol = ""
closing = 0
opening = 0
for i in range(1, n + 1):
    symbol = input()
    if symbol == "(" and current_symbol == "(" or symbol == ")" and current_symbol == ")":
        break
    if symbol == "(":
        closing += 1
        current_symbol = symbol
    elif symbol == ")":
        opening += 1
        current_symbol = symbol
if closing == opening:
    print("BALANCED")
else:
    print("UNBALANCED")