def sgn(x):
    if x == 0:
        return 0
    else:
        return x/abs(x)


File_object = open(r"./AoC/day02/inp.txt", "r")
lines = File_object.readlines()

safety_counter = 0
for line in lines:
    report = line.split()
    for i in range(len(report)-1):
        dif = int(report[i+1]) - int(report[i])
        if abs(dif) == 0 or abs(dif) > 3:
            break
        else:
            if i == 0:
                increase = sgn(dif)
            else:
                if sgn(dif) != increase:
                    break
        if i == len(report)-2:
            safety_counter += 1

print(safety_counter)
