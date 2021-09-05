football_team = input()
ponts = 0
w = 0
d = 0
l = 0
games_played = int(input())
for games in range(1, games_played + 1):
    result = input()
    if result == "W":
        ponts += 3
        w += 1
    elif result == "D":
        ponts += 1
        d += 1
    elif result == "L":
        l += 1
if games_played < 1:
    print(f"{football_team} hasn't played any games during this season.")
else:
    win_rate = w / games_played * 100
    print(f"{football_team} has won {ponts} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {win_rate:.2f}%")
