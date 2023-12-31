import math

class node:
    def __init__(self, inp_name, inp_left, inp_right):
        self.name = inp_name
        self.left = inp_left
        self.right = inp_right

    def match(self, inp_name):
        if(self.name == inp_name):
            return True
        else:
            return False

File_object = open(r"./AoC23/Inp.txt", "r")
lines = File_object.readlines()

directions = lines.pop(0).strip()
ndirections = len(directions)
lines.pop(0)

nodes = []
start_indices = []
for line in lines:
    nodes.append(node(line[0:3], line[7:10], line[12:15]))
    if line[2] == "A":
        start_indices.append(len(nodes) - 1)

n = len(start_indices)
steps = [0]*n

for i in range(n):
    current_node = nodes[start_indices[i]]
    while(current_node.name[2] != "Z"):
        if (directions[steps[i]%ndirections] == "L"):
            next_node_name = current_node.left
        else:
            next_node_name = current_node.right

        for nod in nodes:
            if nod.match(next_node_name):
                current_node = nod
                steps[i] += 1
                break

tot = steps[0]
if n > 1:
    for i in range(1, n):
        tot = math.lcm(tot, steps[i])

print(tot)
