year = input()
holidays = int(input())
weekends_away = int(input())

play_in_sofia = ((48 - weekends_away) * 3 / 4) + (holidays * (2 / 3))

if year == "normal":
    total_play = play_in_sofia + weekends_away
    print(int(total_play))

elif year == "leap":
    total_play = (play_in_sofia + weekends_away) * 1.15
    print(int(total_play))
