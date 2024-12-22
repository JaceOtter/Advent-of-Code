def sgn(x):
    if x == 0:
        return 0
    else:
        return x/abs(x)

def safety_check(report):
    for i in range(len(report)-1):
        dif = int(report[i+1]) - int(report[i])
        if abs(dif) == 0 or abs(dif) > 3:
            return 0
        else:
            if i == 0:
                increase = sgn(dif)
            else:
                if sgn(dif) != increase:
                    return 0
    return 1

File_object = open(r"./AoC/day02/inp.txt", "r")
lines = File_object.readlines()

safety_counter = 0
for line in lines:
    report = line.split()
    if safety_check(report) == 1:
        safety_counter += 1
        continue
    for i in range(len(report)):
        sub_report = list(report[:i] + report[i+1:])
        if safety_check(sub_report) == 1:
            safety_counter += 1
            break

print(safety_counter)
