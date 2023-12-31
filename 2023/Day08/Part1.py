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
for line in lines:
    nodes.append(node(line[0:3], line[7:10], line[12:15]))
    if line[0:3] == "AAA":
        start = len(nodes) - 1

steps = 0
current_node = nodes[start]
print(ndirections)
while(current_node.name != "ZZZ"):
    print(current_node.name, steps%ndirections)
    if (directions[steps%ndirections] == "L"):
        next_node_name = current_node.left
    else:
        next_node_name = current_node.right
    
    for nod in nodes:
        if nod.match(next_node_name):
            current_node = nod
            steps += 1
            break

print(steps)
