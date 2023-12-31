specialChar = [":", ";"]

def splitLine(line):
    n = len(line)
    sep = list()
    for i in range(n):
        if(line[i] in specialChar):
            sep.append(i)
    m = len(sep)
    out = list()
    for i in range(m-1):
        out.append(line[sep[i]+2:sep[i+1]].split(", "))
    out.append(line[sep[-1]+2:].split(", "))
    return out


limits = {"red":12, "green":13, "blue":14}

File_object = open(r"./AoC/Inp02.txt", "r")
lines = File_object.readlines()

# part 1
s = 0
n = len(lines)
for i in range(n):
    skip = False
    game = splitLine(lines[i].rstrip())
    for draw in game:
        for color in draw:
            spl = color.split()
            if (int(spl[0]) > limits[spl[1]]):
                skip = True
                break
        if skip:
            break
    if  not skip:
        s += i + 1

print(s)
            
# part 2
s = 0
for line in lines:
    rgb = {"red":0, "green":0, "blue":0}
    game = splitLine(line.rstrip())
    for draw in game:
        for color in draw:
            spl = color.split()
            rgb[spl[1]] = max(int(spl[0]), rgb[spl[1]])
    s += rgb["red"]*rgb["green"]*rgb["blue"]

print(s)
