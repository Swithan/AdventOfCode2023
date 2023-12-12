from collections import defaultdict



def validate(row, groups):
    gl = 0
    gi = 0
    for item in row:
        if item == '?':
            return None
        elif item == '#':
            gl += 1
        elif gl > 0:
            try:
                if gl != groups[gi]:
                    return False
            except IndexError:
                return False
            gl = 0
            gi += 1
    if gl > 0:
        try:
            if gl != groups[gi]:
                return False
        except IndexError:
            return False
        gi += 1
    gc = len(groups)
    return gi == gc


def get_arangements_slow(row, groups):

    v = validate(row, groups)
    if v is False:
        return 0
    elif v is True:
        return 1

    s = 0
    try:
        first_damage = row.index('?')
    except ValueError:
        if validate(row, groups):
            return 1
        else:
            return 0

    _row = list(row)
    _row[first_damage] = '#'

    s += get_arangements_slow(_row, groups)

    _row = list(row)
    _row[first_damage] = '.'

    s += get_arangements_slow(_row, groups)

    return s


def get_arangement_count(row: str, groups: list):

    group_count = len(groups)
    arangements = dict()
    arangements[0, 0] = 1

    def is_valid(group_index, current_group_size, strict=True):
        try:
            if strict:
                return current_group_size == groups[group_index]
            else:
                return current_group_size <= groups[group_index]
        except IndexError:
            return False

    for c in row:
        new_arangements = defaultdict(int)
        for (group_index, current_group_size), count in arangements.items():
            valid = True
            if c == '#':
                current_group_size += 1
                valid = is_valid(group_index, current_group_size, False)
            elif c == '?':
                # say it's a dot
                if current_group_size > 0:
                    # check if is a valid termination (strict)
                    if is_valid(group_index, current_group_size):
                        new_arangements[group_index + 1, 0] += count
                else:
                    new_arangements[group_index, current_group_size] += count
                # is a hash
                if is_valid(group_index, current_group_size + 1, False):
                    new_arangements[group_index, current_group_size + 1] += count
                continue
            else:
                if current_group_size > 0:
                    # check if is a valid termination (strict)
                    valid = is_valid(group_index, current_group_size)
                    current_group_size = 0
                    group_index += 1
            if valid:
                new_arangements[group_index, current_group_size] += count
        arangements = new_arangements

    c = 0
    for (group_index, current_group_size), count in arangements.items():
        if current_group_size > 0:
            try:
                if current_group_size != groups[group_index]:
                    continue
            except IndexError:
                continue
            group_index += 1
        if group_index == group_count:
            c += count
    return c




def p1(data):
    s = 0
    for row in data.splitlines():
        row, groups = row.split(' ')
        groups = list(map(int, groups.split(',')))
        a = get_arangement_count(row, groups)
        s += a
    print("p1", s)


def p2(data):
    s = 0
    rows = data.splitlines()
    l = len(rows)
    for i, row in enumerate(rows):
        row, groups = row.split(' ')

        row = ((row + '?') * 5)[:-1]

        groups = list(map(int, groups.split(',')))

        groups = groups * 5

        a = get_arangement_count(row, groups)

        # print(f"{i}/{l} -> {a}")

        s += a

    print("p1", s)



#get_arangements('???.###', (1,1,3))
#get_arangements('.??..??...?##.', (1,1,3))
#get_arangements('?#?#?#?#?#?#?#?', (1,3,1,6))
#get_arangements('?###????????', (3,2,1))


data = open("day12.txt", "rt").read().strip()

import time
s = time.time()
p1(data)
p2(data)
print(time.time() - s)