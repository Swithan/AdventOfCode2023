import re
file = list(open("day09.txt"))


def difference(input, last, total):
    output = []
    for i in range(1, len(input)):
        output.append(input[i] - input[i-1])
    if abs(output[-2]) == abs(output[-1]):
        total += last + output[0]
        return total
    total += output[-1]
    total = difference(output, last, total)
    return total


sum = 0
for line in file:
    report = re.findall(r"\d+", line)
    report = [int(i) for i in report]

    total = difference(report, report[-1], 0)
    sum += total

    print("My sum : ", sum)
print("sum")
print(sum)
