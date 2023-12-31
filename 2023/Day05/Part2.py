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

def b_to_a_mapper(b, map):
    a = -1
    for j in range(len(map)):
        if map[j][0] <= b and b < map[j][0] + map[j][2]:
            dif = b - map[j][0]
            a = map[j][1] + dif
            break
    if a == -1:
        a = b
    return a

def in_seed_range(inp, seedranges):
    for i in range(int(len(seedranges)/2)):
        if seedranges[2*i] <= inp and inp < seedranges[2*i] + seedranges[2*i + 1]:
            return True
    return False


File_object = open(r"./AoC/Inp05.txt", "r")
lines = File_object.readlines()

n = len(lines)
linecounter = 0
seedranges = [ int(seed) for seed in lines[linecounter].strip().split(":")[-1].split()]

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


critical_points = list()

for i in range(len(humidity_to_location_map)):
    new = b_to_a_mapper(humidity_to_location_map[i][1], temperature_to_humidity_map)
    if new not in critical_points:
        critical_points.append(new)

temp = list()
for i in range(len(critical_points)):
    new = b_to_a_mapper(critical_points[i], light_to_temperature_map)
    temp.append(new)
critical_points = temp

for i in range(len(temperature_to_humidity_map)):
    new = b_to_a_mapper(temperature_to_humidity_map[i][1], light_to_temperature_map)
    if new not in critical_points:
        critical_points.append(new)

temp = list()
for i in range(len(critical_points)):
    new = b_to_a_mapper(critical_points[i], water_to_light_map)
    temp.append(new)
critical_points = temp

for i in range(len(light_to_temperature_map)):
    new = b_to_a_mapper(light_to_temperature_map[i][1], water_to_light_map)
    if new not in critical_points:
        critical_points.append(new)

temp = list()
for i in range(len(critical_points)):
    new = b_to_a_mapper(critical_points[i], fertilizer_to_water_map)
    temp.append(new)
critical_points = temp

for i in range(len(water_to_light_map)):
    new = b_to_a_mapper(water_to_light_map[i][1], fertilizer_to_water_map)
    if new not in critical_points:
        critical_points.append(new)

temp = list()
for i in range(len(critical_points)):
    new = b_to_a_mapper(critical_points[i], soil_to_fertilizer_map)
    temp.append(new)
critical_points = temp

for i in range(len(fertilizer_to_water_map)):
    new = b_to_a_mapper(fertilizer_to_water_map[i][1], soil_to_fertilizer_map)
    if new not in critical_points and in_seed_range(new, seedranges):
        critical_points.append(new)

temp = list()
for i in range(len(critical_points)):
    new = b_to_a_mapper(critical_points[i], seed_to_soil_map)
    temp.append(new)
critical_points = temp

for i in range(len(soil_to_fertilizer_map)):
    new = b_to_a_mapper(soil_to_fertilizer_map[i][1], seed_to_soil_map)
    if new not in critical_points:
        critical_points.append(new)

for i in range(len(seed_to_soil_map)):
    if seed_to_soil_map[i][1] not in critical_points and in_seed_range(seed_to_soil_map[i][1], seedranges):
        critical_points.append(seed_to_soil_map[i][1])

for i in range(int(len(seedranges)/2)):
    critical_points.append(seedranges[2*i])

#print(critical_points)

nseeds = len(critical_points)
location = [-1]*nseeds
for i in range(nseeds):
    seed = critical_points[i]
    if not in_seed_range(seed, seedranges):
        continue
    soil = a_to_b_mapper(seed, seed_to_soil_map)
    fertilizer = a_to_b_mapper(soil, soil_to_fertilizer_map)
    water = a_to_b_mapper(fertilizer, fertilizer_to_water_map)
    light = a_to_b_mapper(water, water_to_light_map)
    temperature = a_to_b_mapper(light, light_to_temperature_map)
    humidity = a_to_b_mapper(temperature, temperature_to_humidity_map)
    location[i] = a_to_b_mapper(humidity, humidity_to_location_map)
    
m = max(location)
for i in range(nseeds):
    if location[i] == -1:
        location[i] = m

print(min(location))
