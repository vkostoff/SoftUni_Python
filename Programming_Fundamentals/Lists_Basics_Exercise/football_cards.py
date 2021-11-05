team_a_players = 11
team_b_players = 11

sequence_of_cards = set(input().split(sep=" "))
sequence_of_cards = list(sequence_of_cards)

for card in range(0, len(sequence_of_cards)):
    if "A" in sequence_of_cards[card]:
        team_a_players -= 1
        if team_a_players < 7:
            break
            
    elif "B" in sequence_of_cards[card]:
        team_b_players -= 1
        if team_b_players < 7:
            break
            
print(f"Team A - {team_a_players}; Team B - {team_b_players}")

if team_a_players < 7 or team_b_players < 7:
    print("Game was terminated")
