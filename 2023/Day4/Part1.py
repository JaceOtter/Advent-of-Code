File_object = open(r"./AoC/Inp04.txt", "r")
lines = File_object.readlines()

s = 0
for line in lines:
    lin = line.strip().split(":")[-1].split("|")
    winners = lin[0].split()
    players = lin[1].split()
    matches = 0
    for num in players:
        if num in winners:
            matches += 1
    s += int(2**matches/2)

print(s)
