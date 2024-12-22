from collections import Counter

File_object = open(r"./AoC/day01/inp01.txt", "r")
lines = File_object.readlines()

n = len(lines)
first = [0]*n
second = [0]*n
for i in range(n):
    first[i], second[i] = lines[i].split()
    first[i] = int(first[i])
    second[i] = int(second[i])

counts = Counter(second)

sim = 0
for num in first:
    sim += num*counts[num]

print(sim)
