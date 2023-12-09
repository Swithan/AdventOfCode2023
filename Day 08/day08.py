file = list(open("day08.txt"))

instructions = file[0].replace('\n', "")
print(instructions)
file = file[2::]
nodes = {}

for line in file:
    node = line.split(" = ")[0]
    options = line.split('(')[1]
    left = options.split(", ")[0]
    right = options.split(", ")[1].split(")")[0]
    nodes[node] = (left, right)

print(nodes)

steps = 0
curr_pos = "AAA"
while True:
    for side in instructions:

        curr_pos = nodes[curr_pos][0] if side == "L" else nodes[curr_pos][1]
        steps+=1
        if curr_pos == "ZZZ":
            break
    if curr_pos == "ZZZ":
        break
print(steps)

