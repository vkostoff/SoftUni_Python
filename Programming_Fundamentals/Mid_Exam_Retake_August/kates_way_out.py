def find_kate(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == "k":
                return [x, y]


def check_up(position, maze, passed):
    if position[0] > 0:
        if maze[position[0] - 1][position[1]] == " ":
            passed.append([position[0] - 1, position[1]])
            maze[position[0] - 1][position[1]] = "#"
            position[0] -= 1


def check_down(position, maze, rows, passed):
    if position[0] < rows - 1:
        if maze[position[0] + 1][position[1]] == " ":
            passed.append([position[0] + 1, position[1]])
            maze[position[0] + 1][position[1]] = "#"
            position[0] += 1


def check_right(position, maze, passed):
    if (position[1]) < len(maze[0]) - 1:
        if maze[position[0]][position[1] + 1] == " ":
            passed.append([position[0], position[1] + 1])
            maze[position[0]][position[1] + 1] = "#"
            position[1] += 1


def check_left(position, maze, passed):
    if (position[1]) > 0:
        if maze[position[0]][position[1] - 1] == " ":
            passed.append([position[0], position[1] - 1])
            maze[position[0]][position[1] - 1] = "#"
            position[1] -= 1


rows = int(input())
passed = []
maze = []
moves = 0

for i in range(rows):
    row = list(input())
    maze.append(row)
    
position = find_kate(maze)
escaped = False

while True:
    check_up(position, maze, passed)
    check_down(position, maze, rows, passed)
    check_right(position, maze, passed)
    check_left(position, maze, passed)
    
    if position[0] == 0 or position[0] == rows - 1 or position[1] == 0 or position[1] == len(maze[0]) - 1:
        print(f"Kate got out in {len(passed) + 1} moves")
        escaped = True
        break
        
    if maze[position[0]][position[1] + 1] == "#" and maze[position[0]][position[1] - 1] == "#"\
            and maze[position[0] + 1][position[1]] == "#" and maze[position[0] - 1][position[1]] == "#":
        escaped = False
        break

if not escaped:
    print("Kate cannot get out")
