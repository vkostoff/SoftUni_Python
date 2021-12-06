player_pool = {}
total_skill = {}

command = input()
while not command == "Season end":
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        
        if player not in player_pool:
            player_pool[player] = {position: skill}
            
        elif player in player_pool:
            if position not in player_pool[player]:
                player_pool[player].update({position: skill})
                
            elif position in player_pool[player]:
                if player_pool[player][position] < skill:
                    player_pool[player] = {position: skill}
                    
    elif "vs" in command:
        player_one, player_two = command.split(" vs ")
        if player_one in player_pool and player_two in player_pool:
            for k, v in player_pool[player_one].items():
                if k in player_pool[player_two]:
                    if player_pool[player_two][k] > player_pool[player_one][k]:
                        del player_pool[player_one]
                        break
                        
                    elif player_pool[player_two][k] < player_pool[player_one][k]:
                        del player_pool[player_two]
                        break
                        
    command = input()

for k, v in player_pool.items():
    total_skill[k] = 0
    
    for key, value in player_pool[k].items():
        total_skill[k] += value

total_skill_ordered = dict(sorted(total_skill.items(), key=lambda x: (-x[1], x[0])))

for a, b in total_skill_ordered.items():
    print(f"{a}: {b} skill")
    ordered_player = dict(sorted(player_pool[a].items(), key=lambda x: (-x[1], x[0])))
    
    for c, d in ordered_player.items():
        print(f"- {c} <::> {d}")
