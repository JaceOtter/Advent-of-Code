File_object = open(r"./AoC/Inp04.txt", "r")
lines = File_object.readlines()

s = 0
n = len(lines)
wins = [1]*n
for i in range(n):
    lin = lines[i].strip().split(":")[-1].split("|")
    winners = lin[0].split()
    players = lin[1].split()
    matches = 0
    for num in players:
        if num in winners:
            matches += 1
    for j in range(i+1, i+matches+1):
        if j < n:
            wins[j] += wins[i]
    
s = sum(wins)
print(s)
