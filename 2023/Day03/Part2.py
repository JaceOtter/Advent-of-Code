File_object = open(r"./AoC/Inp03.txt", "r")
lines = File_object.readlines()

s = 0
n = len(lines)
part_num = {}
start = False
sp = 0
ep = 0
gears = list()
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
        if c == "*":
            gears.append((i,j))

for gear in gears:
    first = 0
    for key in part_num:
        if key[0] - 1 <= gear[0] and gear[0] <= key[0] + 1 and key[1] - 1 <= gear[1] and gear[1] <= key[2]:
            if first == 0:
                #print(key, part_num[key])
                first = part_num[key]
                continue
            else:
                #print(key, first, part_num[key], s)
                s += first*part_num[key]
                break

print(s)
