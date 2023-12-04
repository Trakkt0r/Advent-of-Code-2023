with open("AoC/input.txt", "r") as input_file:
    main_input = [line.split(": ", 1)[1].replace("\n", "") for line in input_file]

def find_value(matches):

    if matches == 0:
        return 0
        
    return 2 ** (matches-1)


# Efficient solution using set intersections to avoid having to do double nested loops
def part_one(task_input):

    sum = 0

    for line in task_input:

        winning = frozenset(num for num in line.split(" | ")[0].split(" ") if num.isdecimal())
        owned =   frozenset(num for num in line.split(" | ")[1].split(" ") if num.isdecimal())

        sum += find_value(len(winning.intersection(owned)))

    return sum


print(part_one(main_input)) 
