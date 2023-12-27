with open("day15.txt", "r") as file:
    input = file.read().split(',')


def algorithm(clear_string, current_value):
    for char in clear_string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


if __name__ == "__main__":
    results = []
    for string in input:
        current_value = 0
        results.append(algorithm(string, current_value))
    print('part 1 : ' + str(sum(results)))

