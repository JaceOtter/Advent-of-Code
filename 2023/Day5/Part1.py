def a_to_b_mapper(a, map):
    b = -1
    for j in range(len(map)):
        if map[j][1] <= a and a < map[j][1] + map[j][2]:
            dif = a - map[j][1]
            b = map[j][0] + dif
            break
    if b == -1:
        b = a
    return b

def parse_seed_ranges(seedranges):
    n = len(seedranges)
    initial_seed = -1
    out = list()
    for i in range(n):
        if i%2 == 0:
            initial_seed = seedranges[i]
        else:
            for j in range(seedranges[i]):
                out.append(initial_seed + j)
    return out

File_object = open(r"./AoC/test05.txt", "r")
lines = File_object.readlines()

n = len(lines)
linecounter = 0
#seeds = [ int(seed) for seed in lines[linecounter].strip().split(":")[-1].split()]
seedranges = [ int(seed) for seed in lines[linecounter].strip().split(":")[-1].split()]
seeds = parse_seed_ranges(seedranges)

linecounter += 3

seed_to_soil_map = list()
while(linecounter < n):
    line = lines[linecounter].strip().split()
    if not line:
        break
    seed_to_soil_map.append([int(i) for i in line])
    linecounter += 1

linecounter += 2

soil_to_fertilizer_map = list()
while(linecounter < n):
    line = lines[linecounter].strip().split()
    if not line:
        break
    soil_to_fertilizer_map.append([int(i) for i in line])
    linecounter += 1

linecounter += 2

fertilizer_to_water_map = list()
while(linecounter < n):
    line = lines[linecounter].strip().split()
    if not line:
        break
    fertilizer_to_water_map.append([int(i) for i in line])
    linecounter += 1

linecounter += 2

water_to_light_map = list()
while(linecounter < n):
    line = lines[linecounter].strip().split()
    if not line:
        break
    water_to_light_map.append([int(i) for i in line])
    linecounter += 1

linecounter += 2

light_to_temperature_map = list()
while(linecounter < n):
    line = lines[linecounter].strip().split()
    if not line:
        break
    light_to_temperature_map.append([int(i) for i in line])
    linecounter += 1

linecounter += 2

temperature_to_humidity_map = list()
while(linecounter < n):
    line = lines[linecounter].strip().split()
    if not line:
        break
    temperature_to_humidity_map.append([int(i) for i in line])
    linecounter += 1

linecounter += 2

humidity_to_location_map = list()
while(linecounter < n):
    line = lines[linecounter].strip().split()
    if not line:
        break
    humidity_to_location_map.append([int(i) for i in line])
    linecounter += 1


nseeds = len(seeds)
location = [-1]*nseeds
for i in range(nseeds):
    seed = seeds[i]
    soil = a_to_b_mapper(seed, seed_to_soil_map)
    fertilizer = a_to_b_mapper(soil, soil_to_fertilizer_map)
    water = a_to_b_mapper(fertilizer, fertilizer_to_water_map)
    light = a_to_b_mapper(water, water_to_light_map)
    temperature = a_to_b_mapper(light, light_to_temperature_map)
    humidity = a_to_b_mapper(temperature, temperature_to_humidity_map)
    location[i] = a_to_b_mapper(humidity, humidity_to_location_map)
    
print(min(location))



