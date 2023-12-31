from functools import cache

@cache
def count_combos(data, keys, index=0):
    if not data:
        return int(not keys and not index)
    
    #print(data, keys, index)

    s = 0
    choices = [".", "#"] if data[0] == "?" else data[0]
    for c in choices:
        if c == "#":
            s += count_combos(data[1:], keys, index+1)
        else:
            if index > 0:
                if keys:
                    if keys[0] == index:
                        s += count_combos(data[1:], keys[1:])
            else:
                s += count_combos(data[1:], keys)
    return s


File_object = open(r"./AoC23/Day 12/Inp.txt", "r")
lines = File_object.readlines()

s = 0
for line in lines:
    [data, key] = line.strip().split()
    full_data = "?".join([data]*5) + "."
    keys = tuple(5*[ int(k) for k in key.split(",") ])

    s += count_combos(full_data, keys)

#    print(keys)

print(s)

#data = ".###..##...#"
#keys = [3,2,1]
#print(checker(data, keys))

