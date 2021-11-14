n = int(input())
maze = []
for _ in range(n):
    maze.append(list(input()))
pos = []
initial_position = []
moves = 0

for r in range(len(maze)):
    for p in range(len(maze[r])):
        if maze[r][p] == "k":
            pos = r, p
            initial_position.extend(pos)
            current_position = initial_position.copy()
            break

row = initial_position[0]
position = initial_position[1]
right_side = []
left_side = []

still_in_maze = True

for li in range(len(maze)):
    for el in range(len(maze[li])):
        if el == 0:
            right_side.append(maze[li][0])
        elif el == len(maze[li]) - 1:
            left_side.append(maze[li][-1])

max_row = len(maze) - 1
min_row = 0
max_position = len(maze[row]) - 1
min_position = 0

if "k" in maze[0] or "k" in maze[-1] or "k" in right_side or "k" in left_side:
    moves += 1
    still_in_maze = False
    print(f"Kate got out in {moves} moves")

while still_in_maze:
    # check up
    if maze[row - 1][position] == " ":
        maze[row - 1][position] = "#"
        row -= 1
        moves += 1
        if row == min_row or position == max_position:
            moves += 1
            print(f"Kate got out in {moves} moves")
            break
    # check down
    elif maze[row + 1][position] == " ":
        maze[row + 1][position] = "#"
        row += 1
        moves += 1
        if row == max_row or position == max_position:
            moves += 1
            print(f"Kate got out in {moves} moves")
            break
    # check right
    elif maze[row][position + 1] == " ":
        maze[row][position + 1] = "#"
        position += 1
        moves += 1
        if row == min_row or position == max_position:
            moves += 1
            print(f"Kate got out in {moves} moves")
            break
    # check left
    elif maze[row][position - 1] == " ":
        maze[row][position - 1] = "#"
        position -= 1
        moves += 1
        if row == min_row or position == min_position:
            moves += 1
            print(f"Kate got out in {moves} moves")
            break
    else:
        print("Kate cannot get out")
        break
