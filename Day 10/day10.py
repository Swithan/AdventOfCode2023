lines = [s for s in open('day10.txt').read().split('\n') if s.strip()]

print(lines)

links = {
	"|": [(0, -1), (0, 1)],
	"-": [(-1, 0), (1, 0)],
	"L": [(0, -1), (1, 0)],
	"J": [(0, -1), (-1, 0)],
	"7": [(-1, 0), (0, 1)],
	"F": [(1, 0), (0, 1)]
}

s = (0, 0)
for i, l in enumerate(lines):
	if 'S' in l:
		s = (l.index('S'), i)


adjacent = []

i = s[1]
j = s[0]
# Check above
if i > 0:
	if lines[i - 1][j] in ["F", "|", "7"]:
		adjacent.append((j, i - 1))

# Check below
if i < len(lines) - 1:
	if lines[i + 1][j] in ["L", "|", "J"]:
		adjacent.append((j, i+1))
# Check left
if j > 0:
	if lines[i][j - 1] in ["L", "-", "F"]:
		adjacent.append((j - 1, i))

# Check right
if j < len(lines[0]) - 1:
	if lines[i][j + 1] in ["7", "-", "J"]:
		adjacent.append((j + 1, i))

a = [(s[0], s[1]), adjacent[0]]
end = adjacent[1]

now = a[-1]
previous = a[-2]


while now != end:

	symbol = lines[now[1]][now[0]]

	n1 = (now[0]+links[symbol][0][0], now[1]+links[symbol][0][1])
	n2 = (now[0]+links[symbol][1][0], now[1]+links[symbol][1][1])
	next = n1 if n1 != previous else n2

	a.append(next)
	now = a[-1]
	previous = a[-2]

print(len(a)/2)
