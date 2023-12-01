with open("Day 1\input.txt", "r") as input_file:
    main_input = [line.replace("\n", "") for line in input_file]
                       
NUMBERS = "0123456789"
NUMBER_WORDS   = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

MAX_WORD_LEN = 5                                    # main optimization for part 2 :)

def find_in_char_memory(char_memory):               # returns either a character "0" - "9" or None, used in second part

    for number_word in NUMBER_WORDS:

        if number_word in char_memory:

            return str(NUMBER_WORDS[number_word])


def part_one(task_input):

    sum = 0

    for line in task_input:

        first_digit_character = ""                  # storing the first digit as a string instead of int to easily concatenate later

        for character in line:

            if character in NUMBERS:

                first_digit_character = character
                break

        for character in reversed(line):            # looking through the reversed line is faster, we don't need to loop throuh the middle

            if character in NUMBERS:

                sum += int(first_digit_character + character)   # add the result to sum straight away, there isn't anything else to do with it
                break

    return sum


def part_two(task_input):

    sum = 0

    for line in task_input:

        char_memory             = ""                    # FIFO, at most MAX_WORD_LEN length, use: finding word num  
        first_digit_character   = ""


        # First number find

        for character in line:

            if character in NUMBERS:

                first_digit_character = character
                break

            char_memory += character                    

            first_digit_character = find_in_char_memory(char_memory[-MAX_WORD_LEN:])            # Adds to char_memory from the right

            if first_digit_character:                   # I believe this is the only way to compute it and check if it even
                break                                   # exists without rerunning the function again, it's pretty expensive
        
        char_memory = ""                                # Even though not resetting it didn't cause any issues, I believe it could

        # Last number add to first

        for character in reversed(line):

            if character in NUMBERS:

                sum += int(first_digit_character + character)
                break

            char_memory += character

            found_character = find_in_char_memory(char_memory[:-MAX_WORD_LEN-1:-1])             # Adds to char_memory add from the left

            if found_character:

                sum += int(first_digit_character + found_character)
                break

    return sum


print(part_one(main_input))
print(part_two(main_input))
