with open("Day 3\input.txt", "r") as input_file:
    main_input = [line.replace("\n", "") for line in input_file]                       

# Used in both parts, this function returns the amount of unique 
def find_numeric_neighbors(task_input, x, y):

    line_amount = len(task_input)           # Max Y bound
    line_length = len(task_input[y])        # Max X bound

    offsets = (-1, 0, 1)                    # This is the possible offsets for both x, y -> 3^2 = 9, ignore (0, 0) = itself -> 8 possible choices

    # Makes sure a neighbor is not out of the bounds of the list, is not itself and that it is a number :)
    existing_neighbors = [(x+x_off, y+y_off) for x_off in offsets for y_off in offsets if 0 <= x+x_off< line_length and 0 <= y+y_off < line_amount and (x_off != 0 or y_off != 0) and task_input[y+y_off][x+x_off].isnumeric()]

    # This gets only one point per unique part number
    unique_part_neighbors = [unique for unique in existing_neighbors if not (unique[0]+1, unique[1]) in existing_neighbors]

    return unique_part_neighbors


# Used in both parts, this function will take in any point in the grid and find the rest of the part number it hit
def find_rest_of_number(task_input, x, y):

    line = task_input[y]
    line_length = len(line) 
    number = ""                             # String for easier concatenation

    for i in range(x, -1, -1):
        
        if not line[i].isnumeric():
            x = i+1
            break

        x = 0

    for i in range(x, line_length):
        
        if not line[i].isnumeric():
            return int(number)
        
        number += line[i]

    return int(number)
        

def part_one(task_input):

    sum = 0

    for y in range(len(task_input)):

        line = task_input[y]

        for x in range(len(line)):

            character = line[x]

            if character == "." or character.isnumeric():
                continue
            
            for neighbor in find_numeric_neighbors(main_input, x, y):
                sum += find_rest_of_number(main_input, neighbor[0], neighbor[1])

    return str(sum)
                

def part_two(task_input):

    sum = 0

    for y in range(len(task_input)):

        line = task_input[y]

        for x in range(len(line)):

            character = line[x]

            # While these could be compacted into 1 if statement, most characters 
            # aren't "*", therefore it would make this code many times slower

            if character != "*":
                continue

            numeric_neighbors = find_numeric_neighbors(main_input, x, y)

            if len(numeric_neighbors) != 2:
                continue

            sum += find_rest_of_number(main_input, *numeric_neighbors[0][:2]) * find_rest_of_number(main_input, *numeric_neighbors[1][:2])

    return sum


print("Part 1:", part_one(main_input))
print("Part 2:", part_two(main_input))
