from itertools import product, combinations

with open("Day 11\input_test.txt", "r") as input_file:
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
            main_input[main_input.index(line)] = line[:column] + "X" + line[column:]

    line_length = len(main_input[0])

    for row in sorted(list(empty_rows), reverse=True):
        main_input.insert(row, line_length * "X")

    for row in main_input:
        print(row)

def find_all_galaxies(task_input):

    galaxy_positions = []

    for y, line in enumerate(main_input):
        for x, character in enumerate(line):
            if character == "#":
                galaxy_positions.append((x, y))

    return galaxy_positions

def part_one(task_input):

    sum = 0
    galaxy_coordinates = find_all_galaxies(task_input)

    for coordinate_tuple in combinations(galaxy_coordinates, 2):

        for i in range(2):
            sum += abs(coordinate_tuple[0][i] - coordinate_tuple[1][i])
        
    return sum


print(part_one(main_input))
