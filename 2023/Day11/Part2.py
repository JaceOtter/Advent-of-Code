File_object = open(r"./AoC23/Day 11/Inp.txt", "r")
lines = File_object.readlines()

n = len(lines)
m = len(lines[0])

stars = []
for i in range(n):
    for j in range(m-1):
        if lines[i][j] == "#":
            stars.append((i,j))

expand_rows = []
for i in range(n):
    skip = False
    for P in stars:
        if i == P[0]:
            skip = True
            break
    if not skip:
        expand_rows.append(i)

expand_columns = []
for i in range(m-1):
    skip = False
    for P in stars:
        if i == P[1]:
            skip = True
            break
    if not skip:
        expand_columns.append(i)

#print(stars)
#print(expand_columns)
#print(expand_rows)

expanded = [expand_rows, expand_columns]

dist = 0
nstars = len(stars)
for i in range(nstars-1):
    for j in range(i+1,nstars):
        star1 = stars[i]
        star2 = stars[j]
#        print(star1, star2)
        dist += abs(star2[0] - star1[0]) + abs(star2[1] - star1[1])
        for index in range(2):
            if star1[index] < star2[index]:
                r = range(star1[index], star2[index])
            else:
                r = range(star2[index], star1[index])
            for k in expanded[index]:
                if k in r:
                    dist += 999999

print(dist)
