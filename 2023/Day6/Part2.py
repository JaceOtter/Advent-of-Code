def append_list(strings):
    out = ""
    for string in strings:
        out += string
    return out

File_object = open(r"./AoC23/Inp06.txt", "r")
lines = File_object.readlines()

T = int(append_list([ t for t in lines[0].strip().split(":")[-1].split()]))
dist_thresh = int(append_list([ d for d in lines[1].strip().split(":")[-1].split()]))

wins = 0
dif = 0
for t in range(int(T/2),0,-1):
    if t*(T-t) <= dist_thresh:
        dif = int(T/2) - t
        break
wins = 2*dif
if T%2 == 0:
    wins -= 1

print(wins)
