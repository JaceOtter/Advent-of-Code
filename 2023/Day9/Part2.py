

File_object = open(r"./AoC23/Day 9/Inp.txt", "r")
lines = File_object.readlines()

tot = 0
for line in lines:
    sequence = [int(i) for i in line.strip().split()]
    current_sequence = sequence
    first = []

    while(not all([ v == 0 for v in current_sequence ])):
        dif = [current_sequence[i]-current_sequence[i-1] for i in range(1,len(current_sequence))]
        first.insert(0, dif[0])
        current_sequence = dif
#        print(current_sequence)

#    print(first)

    new = []
    new.append(first[0])
    for i in range(1, len(first)):
        new.append(first[i] - new[-1])

#    print(new)
    tot += sequence[0] - new[-1]

print(tot)
