def direction(s):
    if s == "|":
        return "NS"
    if s == "-":
        return "EW"
    if s == "L":
        return "NW"
    if s == "J":
        return "NE"
    if s == "7":
        return "SE"
    if s == "F":
        return "SW"

File_object = open(r"./AoC23/Day 10/Inp.txt", "r")
lines = File_object.readlines()

n = len(lines)
maze = []
path = {}
for i in range(n):
    maze.append(lines[i].strip())
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            path[(i,j)] = 0

m = len(maze[0])
start = list(path.keys())[0]
directions = ""
if start[0] > 0:
    if maze[start[0]-1][start[1]] in ["7", "|", "F"]:
        directions += "N"
if start[0] < n:
    if maze[start[0]+1][start[1]] in ["J", "|", "L"]:
        directions += "S"
if start[1] > 0:
    if maze[start[0]][start[1]-1] in ["L", "-", "F"]:
        directions += "E"
if start[1] < m:
    if maze[start[0]][start[1]+1] in ["J", "-", "7"]:
        directions += "W"

#print(directions)

current_points = [start, start]

step = 0
while(directions):
    step += 1
#    print(current_points)
#    print(directions)
    for i in range(len(current_points)):
        path_points = list(path.keys())
        P = current_points[i]
        if directions[i] == "N":
            NP = (P[0]-1, P[1])
            if NP not in path_points:
                path[NP] = step
        elif directions[i] == "S":
            NP = (P[0]+1, P[1])
            if NP not in path_points:
                path[NP] = step
        elif directions[i] == "E":
            NP = (P[0], P[1]-1)
            if NP not in path_points:
                path[NP] = step
        elif directions[i] == "W":
            NP = (P[0], P[1]+1)
            if NP not in path_points:
                path[NP] = step

#    print(path)

    current_points = [P for P in list(path.keys()) if path[P] == step]
    directions = ""
    path_points = list(path.keys())
    for P in current_points:
        D = direction(maze[P[0]][P[1]])
        for i in range(len(D)):
            if D[i] == "N" and (P[0]-1, P[1]) not in path_points:
                directions += "N"
                break
            if D[i] == "S" and (P[0]+1, P[1]) not in path_points:
                directions += "S"
                break
            if D[i] == "E" and (P[0], P[1]-1) not in path_points:
                directions += "E"
                break
            if D[i] == "W" and (P[0], P[1]+1) not in path_points:
                directions += "W"
                break

print(step)
