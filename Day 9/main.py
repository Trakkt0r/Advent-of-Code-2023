with open("Day 9\input.txt", "r") as input_file:
    # main_input is a list of tuples of the integers of a sequence
    main_input = [tuple(map(lambda x: int(x), line.replace("\n", "").split(" "))) for line in input_file if line != "\n"]


def get_next_sequence(sequence):

    next_sequence = []

    for i in range(len(sequence)-1):
        next_sequence.append(sequence[i+1] - sequence[i])

    return tuple(next_sequence)


def is_all_zeros(sequence): 

    if type(sequence) != (tuple or list):
        return None

    if len(sequence) > 1:
        return set(sequence) == {0}
    
    return sequence[0] == 0


def get_sequence_pyramid(start_sequence):

    sequence_pyramid = [start_sequence]

    while True:

        sequence_pyramid.append(get_next_sequence(sequence_pyramid[-1]))
        last_sequence = sequence_pyramid[-1]

        if is_all_zeros(last_sequence) or len(last_sequence) == 1:
            break

    return sequence_pyramid


def part_one(task_input):

    sum = 0

    for line in task_input:

        sequence_pyramid = get_sequence_pyramid(line)

        # the next number is just the sum of last numbers in each seq and we add up the next nums
        for sequence in sequence_pyramid:
            sum += sequence[-1]

    return sum


def part_two(task_input):

    sum = 0

    for line in task_input:

        current_value = 0
        sequence_pyramid = get_sequence_pyramid(line)

        # goes through sequence_pyramid in reverse order, ignoring the all zeros tuple
        for sequence in sequence_pyramid[-2::-1]:
            current_value = sequence[0] - current_value

        sum += current_value

    return sum

print(part_one(main_input))
print(part_two(main_input))
