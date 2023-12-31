
File_object = open(r"./AoC23/Inp06.txt", "r")
lines = File_object.readlines()

times = [ int(time) for time in lines[0].strip().split(":")[-1].split()]
dist_thresh = [ int(d) for d in lines[1].strip().split(":")[-1].split()]

n = len(times)
prod = 1
#wins = [0]*n
for i in range(n):
    wins = 0
    T = times[i]
    dif = 0
    for t in range(int(T/2),0,-1):
        if t*(T-t) <= dist_thresh[i]:
            dif = int(T/2) - t
            break
    wins = 2*dif
    if T%2 == 0:
        wins -= 1
    prod *= wins

print(prod)
