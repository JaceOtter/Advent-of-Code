def generate_combos(spring_record, index):
    if index >= len(spring_record):
        return [spring_record]
    
    if spring_record[index] == "?":
        dot = generate_combos(spring_record[:index] + "." + spring_record[index+1:], index + 1)
        pound = generate_combos(spring_record[:index] + "#" + spring_record[index+1:], index + 1)
        return dot + pound
    else:
        return generate_combos(spring_record, index + 1)

def checker(data, keys):
    data_split = []
    for d in data.strip(".").split("."):
        if d != '':
            data_split.append(d)
    n = len(keys)
    if len(data_split) != n:
        return False
    for i in range(n):
        if len(data_split[i]) != keys[i]:
            return False
    return True


File_object = open(r"./AoC23/Day 12/Inp.txt", "r")
lines = File_object.readlines()

s = 0
for line in lines:
    [data, key] = line.strip().split()
    keys = [ int(k) for k in key.split(",") ]

    combos = generate_combos(data, 0)
#    print(data)
#    print(combos)
    for combo in combos:
        if checker(combo, keys):
            s += 1

#    print(keys)

print(s)

#data = ".###..##...#"
#keys = [3,2,1]
#print(checker(data, keys))
