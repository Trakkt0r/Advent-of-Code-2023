from itertools import product, combinations

with open("Day 11\input.txt", "r") as input_file:
    main_input = [line.replace("\n", "") for line in input_file]

    # everything below in this scope is responsible for adding in the expansions of the universe
    empty_columns, empty_rows = {i for i in range(len(main_input[0]))}, {i for i in range(len(main_input))}

    for coordinate in product(empty_rows, empty_columns):
        y, x = coordinate

        if main_input[y][x] != ".":
            empty_rows.discard(y)
            empty_columns.discard(x)


    for column in sorted(list(empty_columns), reverse=True):
        for line in main_input:
            main_input[main_input.index(line)] = line[:column] + "X" + line[column + 1:]

    line_length = len(main_input[0])

    for row in sorted(list(empty_rows), reverse=True):
        main_input[row] = line_length * "X"


def find_all_galaxies(task_input):

    galaxy_positions = []

    for y, line in enumerate(main_input):
        for x, character in enumerate(line):
            if character == "#":
                galaxy_positions.append((x, y))

    return galaxy_positions


def count_empty_interceptions(coordinate1, coordinate2):

    interception_count = 0
    x1, y1 = coordinate1
    x2, y2 = coordinate2

    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)

    for column in empty_columns:
        if x_min < column < x_max:
            interception_count += 1

    for row in empty_rows:
        if y_min < row < y_max:
            interception_count += 1

    return interception_count


def main(task_input, empty_space_size):

    sum = 0
    galaxy_coordinates = find_all_galaxies(task_input)

    for coordinate_tuple in combinations(galaxy_coordinates, 2):

        for i in range(2):
            sum += abs(coordinate_tuple[0][i] - coordinate_tuple[1][i])
        
        sum += count_empty_interceptions(*coordinate_tuple) * empty_space_size

    return sum


print("Part 1:", main(main_input, 1))
print("Part 2:", main(main_input, 1e6-1))
