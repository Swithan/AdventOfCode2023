file = [s for s in open('day14.txt').read().split('\n') if s.strip()]


def check_vertical(pattern):
	columns = ["" for i in range(len(pattern[0]))]
	for p in pattern:
		for i, c in enumerate(p):
			columns[i] += c
	return columns




vertical = check_vertical(file)

tilt = []
load = len(vertical[0])

for v in vertical:
	last_o_index = v.rfind('O')

	if last_o_index != -1:
		tilt.append(v[:last_o_index + 1])
x = []
for t in tilt:
	s = t.split("#")
	index = 0
	a = 0
	sub_total = 0
	for p in s:
		for i, c in enumerate(p):
			if c == "O":
				sub_total += load - (i + index) + a
			else:
				a += 1
		a = 0
		index += len(p)+1
	x.append(sub_total)

print(sum(x))