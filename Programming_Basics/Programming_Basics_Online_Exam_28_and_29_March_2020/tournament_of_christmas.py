tournament_days = int(input())
command = input()
money_won = 0
games_won = 0
games_lost = 0
for days in range(1, tournament_days + 1):
    money_won_today = 0
    games_won_today = 0
    games_lost_today = 0
    while command != "Finish":
        sport = str(command)
        result = input()
        if result == "win":
            money_won_today += 20
            games_won += 1
            games_won_today += 1
        elif result == "lose":
            games_lost += 1
            games_lost_today += 1
        if games_won_today > games_lost_today:
            money_won_today *= 1.1
            money_won = money_won_today
        else:
            money_won = money_won_today
        command = input()

if games_won > games_lost:
    money_won *= 1.2
    print(f"You won the tournament! Total raised money: {money_won:.2f}")
if games_won < games_lost:
    print(f"You lost the tournament! Total raised money: {money_won:.2f}")
