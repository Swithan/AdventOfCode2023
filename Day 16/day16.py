with open("day16.txt", "r") as file:
    content = file.read()

modified_content = content.replace('\\', 'V')

with open("day16.txt", "w") as file:
    file.write(modified_content)

with open("day16.txt", "r") as file:
    input = file.read().split('\n')


def create_output(input):
    output = ["." * len(input[0]) for i in range(len(input[0]))]
    output[0] = "r" + output[0][1:]
    return output


def move(layout, x, y, direction):
    match direction:
        case 'up':
            if y - 1 >= 0:
                return x, y - 1

        case 'right':
            if x + 1 < len(layout[0]):
                return x+1, y

        case 'down':
            if y + 1 < len(layout):
                return x, y+1

        case 'left':
            if x-1 >= 0:
                return x-1, y
    return -1, -1


def change_direction(direction, action):
    match action:
        case "/":
            match direction:
                case "up":
                    return ["right"]
                case "right":
                    return ["up"]
                case "down":
                    return ["left"]
                case "left":
                    return ["down"]
        case "V":
            match direction:
                case "up":
                    return ["left"]
                case "right":
                    return ["down"]
                case "down":
                    return ["right"]
                case "left":
                    return ["up"]
        case "-":
            if direction == "left" or direction == "right":
                return [direction]
            else:
                return ["left", "right"]
        case "|":
            if direction == "up" or direction == "down":
                return [direction]
            else:
                return ["up", "down"]


def make_move(layout, x, y, direction, output):

    next_x, next_y = move(layout, x, y, direction)
    if (next_y == -1 and next_x == -1) or output[next_y][next_x] == direction[0]:
        return output
    else:
        output[next_y] = output[next_y][:next_x] + direction[0] + output[next_y][next_x+1:]

    if layout[next_y][next_x] == '.':
        output = make_move(layout, next_x, next_y, direction, output)
    else:
        next_directions = change_direction(direction, layout[next_y][next_x])
        for next_dir in next_directions:
            output = make_move(layout, next_x, next_y, next_dir, output)
    return output


def handle_move(layout, x, y, direction, output):
    last_x = x
    last_y = y

    x, y = move(layout, x, y, direction)
    output[last_y] = output[last_y][:last_x] + "#" + output[last_y][last_x + 1:]
    if output[y][x] == "#" or (x == -1 and y == -1):
        return output

    if layout[y][x] == ".":
        output = handle_move(layout, x, y, direction, output)
        print(output)
    else:
        new_directions = change_direction(direction, layout[y][x])
        if type(new_directions) == list:
            for d in new_directions:
                output = handle_move(layout, x, y, d, output)
                print(output)
        else:
            output = handle_move(layout, x, y, new_directions, output)
        print(output)
    return output


def part1(layout, energized):
    print(layout)
    y = 0
    x = 0
    direction = change_direction("right", layout[y][x])[0]
    # result = handle_move(layout, x, y, direction, energized)
    result = make_move(layout, x, y, direction, energized)
    print(result)
    total = 0
    for line in result:
        for char in line:
            if char != ".":
                total += 1
    return total


if __name__ == "__main__":
    output = create_output(input)
    results1 = part1(input, output)

    print('part 1 : ' + str(results1))

    # results2 = part2(input)
    # print('part 2 : ' + str(results2))

