import re

with open("day05.txt") as file:
    file = [l for l in file]
    seeds = file[0]
    seeds = re.findall(r'\d+', seeds)

    maps = []
    start = False
    map = []
    for line in file:
        if start:
            if '\n' == line:
                maps.append(tuple(map))
                map.clear()
                start = False
                continue
            map.append(line)
        if 'map:' in line:
            start = True
    
    final = []
    for seed in seeds:
        out = int(seed)
        for map in maps:
            start_ranges = []
            end_ranges = []
            for range in map:
                parts = re.findall(r'\d+', range)
                start_ranges.append((parts[1], str(int(parts[1])+int(parts[2]))))
                end_ranges.append((parts[0], str(int(parts[0])+int(parts[2]))))
                if out >= int(parts[1]) and out <= int(parts[1])+int(parts[2]):
                    out = int(parts[0]) + int(out - int(parts[1]))
                    break
        final.append((seed, out))
    print(final)

    min = final[0]
    for i in final:
        if i[1] < min[1]:
            min = i
    print(min)
#for each seed:
    #for each range
        # check if in range source-range-start (column 2) (a>src-rng-start && a<src-rng-end (which is src-rng-start+range-length))
        # if YES :
            # compute new destination-range-end value on destination-range-start at index (which is seed-number - source-range-start)
    # IF NO (else), keep seed number
    # REPEAT ABOVE AT EACH STEPS