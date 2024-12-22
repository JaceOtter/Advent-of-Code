
File_object = open(r"./AoC/day01/inp.txt", "r")
lines = File_object.readlines()

n = len(lines)
first = [0]*n
second = [0]*n
for i in range(n):
    first[i], second[i] = lines[i].split();
    first[i] = int(first[i])
    second[i] = int(second[i])

first.sort()
second.sort()

dif = 0
for i in range(n):
    dif += abs(first[i] - second[i])

print(dif)
