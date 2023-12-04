# Efficient solution using set intersections to avoid having to do double nested loops when checking for matches

from collections import Counter

with open("Day 4\input.txt", "r") as input_file:
    main_input = [line.split(": ", 1)[1].replace("\n", "") for line in input_file]

def find_value(matches):

    if not matches:
        return 0
        
    return 2 ** (matches-1)


def part_one(task_input):

    sum = 0

    for line in task_input:

        winning = frozenset(num for num in line.split(" | ")[0].split(" ") if num.isdecimal())
        owned   = frozenset(num for num in line.split(" | ")[1].split(" ") if num.isdecimal())

        sum += find_value(len(winning.intersection(owned)))

    return sum


def part_two(task_input):

    max_card_number = len(task_input)+1
    card_number     = 0
    card_counter    = Counter({x:1 for x in range(1, max_card_number)})

    for line in task_input:

        card_number += 1
    
        winning     = frozenset(num for num in line.split(" | ")[0].split(" ") if num.isdecimal())
        owned       = frozenset(num for num in line.split(" | ")[1].split(" ") if num.isdecimal())

        # This line adds the amount of {the current card} to the next {amount of matches} cards, also makes sure the copies don't exceed the last card
        card_counter.update({card_number + i: card_counter[card_number] for i in range(1, 1 + len(winning.intersection(owned))) if card_number + i <= max_card_number})

    return card_counter.total()


print(part_one(main_input))
print(part_two(main_input))
