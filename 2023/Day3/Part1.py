File_object = open(r"./AoC/Inp03.txt", "r")
lines = File_object.readlines()

s = 0
n = len(lines)
part_num = {}
start = False
sp = 0
ep = 0
for i in range(n):
    m = len(lines[i].strip())
    for j in range(m):
        c = lines[i][j]
        if c.isdigit():
            if not start and j != m - 1:
                start = True
                sp = j
        else:
            if start:
                start = False
                ep = j
                part_num[(i,sp,ep)] = int(lines[i][sp:ep])
        if j == m-1 and start:
            start = False
            ep = j
            part_num[(i,sp,ep)] = int(lines[i][sp:])
            print(i,sp,ep, part_num[(i,sp,ep)])            

for key in part_num:
    #print(key, s)
    if key[1] != 0:
        st = key[1] - 1
    else:
        st = key[1]

    if key[2] != m - 1:
        end = key[2] + 1
    else:
        end = key[2]

    if not lines[key[0]][st].isdigit() and lines[key[0]][st] != ".":
        s += part_num[key]
        continue

    if not lines[key[0]][end-1].isdigit() and lines[key[0]][end-1] != ".":
        s += part_num[key]
        continue

    for i in range(st, end):
        if key[0] != 0:
            if not lines[key[0]-1][i].isdigit() and lines[key[0]-1][i] != ".":
                s += part_num[key]
                break
        if key[0] != n-1:
            if not lines[key[0]+1][i].isdigit() and lines[key[0]+1][i] != ".":
                s += part_num[key]
                break

print(s)
