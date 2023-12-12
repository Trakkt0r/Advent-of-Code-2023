from collections import Counter

TYPES = {(5,): "7", (4, 1): "6", (3, 2): "5", (3, 1): "4", (2, 2): "3", (2, 1): "2", (1, 1): "1"}

with open("Day 7\input.txt", "r") as input_file:

    def transform_input(inp):
        if inp.isdecimal():
            return int(inp)

        # this will convert it so that it's representable as a hexadecimal number
        # ace gets replaced first to avoid replacement collisions (T turns into A)

        return inp.replace("A", "E").replace("T", "A").replace("J", "B").replace("Q", "C").replace("K", "D")

    # hand, bid tuples; both parts are transformed for convenience later in the code
    # it's more convenient as a dictionary, although idk how to make it using dict comp 

    main_input = [tuple(map(transform_input, line.replace("\n", "").split(" "))) for line in input_file]
    main_input = {k:v for (k, v) in main_input}


# the following two functions are similar in what they do, they generate a number for sort() to compare with
# the first digit is from the TYPES, five of a kind being the highest (7), high card being lowest (1)
# the remaining digits are just the hand, hence why we converted it to a "hexadecimable" format
# fortunately that works thanks to the significance of digits going from left to right, so type is most
# important, if they match the first card of hand is next, then second, all the way down to last 

def get_sort_value_p1(hand):
    hand = str(hand)
    return int(TYPES[tuple([common[1] for common in Counter(hand).most_common(2)])] + hand, 16)


def get_sort_value_p2(hand):

    hand = str(hand).replace("B", "1")          # this is for the hand (not first digits), since it doesn't affect typing in any way

    # this part is responsible for replacing a "1" - that is a joker - with a different card, which will benefit the typing the most
    # thanks to the counter approach, adding to the most frequent card given by Counter.most_common(n)[0][0] will always find the best option
    # unless the most frequent one is a "1" (i.e. joker), where we instead look for the second most common with Counter.most_common(n)[1][0]
    
    hand_counter_val = Counter(hand).most_common(2)[0][0]
    if hand_counter_val == "1" and hand != "11111":
        hand_counter_val = Counter(hand).most_common(2)[1][0]

    return int(TYPES[tuple([common[1] for common in Counter(hand.replace("1", hand_counter_val)).most_common(2)])] + hand, 16)


def main(task_input, sort_function):

    sum   = 0
    hands = []

    for bet in task_input:
        hands.append(bet)

    hands.sort(key=sort_function)

    for i in range(len(hands)):
        sum += (i+1)*task_input[hands[i]]

    return sum


print("Part 1:", main(main_input, get_sort_value_p1))
print("Part 2:", main(main_input, get_sort_value_p2))
