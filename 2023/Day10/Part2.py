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

def piece(s):
    if s == "NS":
        return "|"
    if s == "EW":
        return "-"
    if s == "NW":
        return "L"
    if s == "NE":
        return "J"
    if s == "SE":
        return "7"
    if s == "SW":
        return "F"

def flip_switch(b):
    return not b

File_object = open(r"./AoC23/Day 10/Inp.txt", "r")
lines = File_object.readlines()

n = len(lines)
maze = []
path = []
for i in range(n):
    maze.append(lines[i].strip())
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            path.append((i,j))

m = len(maze[0])
start = path[0]
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

maze[start[0]] = maze[start[0]][0:start[1]] + piece(directions) + maze[start[0]][start[1]+1:]
current_point = start

while(directions):
    for i in range(len(directions)):
        P = current_point
        if directions[i] == "N":
            NP = (P[0]-1, P[1])
        elif directions[i] == "S":
            NP = (P[0]+1, P[1])
        elif directions[i] == "E":
            NP = (P[0], P[1]-1)
        elif directions[i] == "W":
            NP = (P[0], P[1]+1)
        if NP not in path:
            path.append(NP)

    current_point = NP
    directions = ""
    P = current_point
    D = direction(maze[P[0]][P[1]])
    for i in range(len(D)):
        if D[i] == "N" and (P[0]-1, P[1]) not in path:
            directions += "N"
            break
        if D[i] == "S" and (P[0]+1, P[1]) not in path:
            directions += "S"
            break
        if D[i] == "E" and (P[0], P[1]-1) not in path:
            directions += "E"
            break
        if D[i] == "W" and (P[0], P[1]+1) not in path:
            directions += "W"
            break

inside = False
up = False

#for i in range(n):
#    line = ""
#    for j in range(m):
#        if (i,j) in path:
#            line += "p"
#        else:
#            line += "."
#    print(line)

area = 0
for i in range(n):
#for i in range(0,5):
#    print(i)
    for j in range(m):
#        print(inside)
        if (i,j) in path and maze[i][j] == "|":
            inside = flip_switch(inside)
        if (i,j) in path and maze[i][j] == "F":
            up = False
        elif (i,j) in path and maze[i][j] == "L":
            up = True
        elif (i,j) in path and maze[i][j] == "J":
            if not up:
                inside = flip_switch(inside)
        elif (i,j) in path and maze[i][j] == "7":
            if up:
                inside = flip_switch(inside)
        elif (i,j) not in path:
            if inside:
                area += 1

print(area)
