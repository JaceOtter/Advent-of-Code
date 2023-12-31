

File_object = open(r"./AoC23/Day 9/Inp.txt", "r")
lines = File_object.readlines()

tot = 0
for line in lines:
    sequence = [int(i) for i in line.strip().split()]
    current_sequence = sequence
    last = []

    while(not all([ v == 0 for v in current_sequence ])):
        dif = [current_sequence[i]-current_sequence[i-1] for i in range(1,len(current_sequence))]
        last.insert(0, dif[-1])
        current_sequence = dif

    new = []
    new.append(last[0])
    for i in range(1, len(last)):
        new.append(last[i] + new[-1])

    tot += sequence[-1] + new[-1]

print(tot)
