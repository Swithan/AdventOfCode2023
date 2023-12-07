import re
with open('./day02.txt') as f:
    counts = []
    for l in f:
        l = l.split(": ")[1]
        sets = l.split("; ")

        colors = {"red": 0, "green": 0, "blue": 0}
        for set in sets :
            results = set.split(", ")
            for color in colors.keys():
                for result in results:
                    if color in result:
                        value = int(re.findall(r'\d+', result)[0])
                        colors[color] = max(colors[color], value)
        counts.append(colors)
    check = {"red": 12, "green": 13, "blue": 14}
    ids = 0
    for i, count in enumerate(counts):
        for color in check.keys():
            if check[color] < count[color]:
                break
        else:
            ids += i + 1
    print(ids)

    power = 0
    for count in counts:
        power += count["red"]*count["green"]*count["blue"]
    print(power)
    f.close()