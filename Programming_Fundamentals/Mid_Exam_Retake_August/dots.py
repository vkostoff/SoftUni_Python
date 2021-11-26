def check_up(maze):
    if maze[r] > 0:
        if maze[r - 1][l] == ".":
            pass


rows = int(input())
maze = []
passed = []
max_dots = 0
current_dots = 0
for i in range(rows):
    maze.append(input().split())
for r in range(len(maze)):
    for l in range(len(maze[r])):
        if maze[r][l] == ".":
            print("yes")
        else:
            print("no")



print(maze)
