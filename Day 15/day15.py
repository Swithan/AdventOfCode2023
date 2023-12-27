with open("day15.txt", "r") as file:
    input = file.read().split(',')


def algorithm(clear_string, current_value):
    for char in clear_string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part1(input):
    results = []
    for string in input:
        current_value = 0
        results.append(algorithm(string, current_value))
    return results


def lenses(input):
    box = 0
    boxes = {i: [] for i in range(256)}
    for string in input:
        current_value = 0
        label = string.split("=")
        if len(label) == 2:
            box = algorithm(label[0], current_value)
            exists = False
            for i, b in enumerate(boxes[box]):
                if label[0] == b[0]:
                    boxes[box][i] = (label[0], label[1])
                    exists = True
                    break
            if not exists:
                boxes[box].append((label[0], label[1]))
        else:
            label = string.split('-')[0]
            for bx in boxes.keys():
                if len(boxes[bx]) > 0:
                    for b in boxes[bx]:
                        if label == b[0]:
                            boxes[bx].remove(b)
                            break
    return boxes


def part2(input):
    total = 0
    boxes = lenses(input)
    for box in boxes:
        if len(boxes[box]) > 0:
            for i, b in enumerate(boxes[box]):
                total += (box + 1) * (i+1) * int(b[1])
    return total


if __name__ == "__main__":
    results1 = part1(input)
    print('part 1 : ' + str(sum(results1)))

    results2 = part2(input)
    print('part 2 : ' + str(results2))

