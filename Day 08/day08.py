import math
file = list(open("day08.txt"))

instructions = file[0].replace('\n', "")

file = file[2::]
nodes = {}

for line in file:
    node = line.split(" = ")[0]
    options = line.split('(')[1]
    left = options.split(", ")[0]
    right = options.split(", ")[1].split(")")[0]
    nodes[node] = (left, right)


starts = []
ends = []
for node in nodes.keys():
    if node[2] == "A": starts.append(node)
    elif node[2] == "Z": ends.append(node)

lcm = []
for start in starts:
    steps = 0

    curr_pos = start

    while True:
        for side in instructions:

            curr_pos = nodes[curr_pos][0] if side == "L" else nodes[curr_pos][1]
            steps+=1
            if curr_pos in ends:
                break
        if curr_pos in ends:
            break
    lcm.append(steps)

result = 1

for i in lcm:
    result = result*i//math.gcd(result, i)
print(result)