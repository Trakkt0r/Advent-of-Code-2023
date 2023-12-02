with open("Day 2\input.txt", "r") as input_file:
    main_input = [line.replace("\n", "")[5:] for line in input_file]

colors = {"red": 12, "green": 13, "blue": 14}

def parse_line(line):                                   # used in both parts; returns game_id, and a list of all drawn sets

    game_id, draws_string = line.split(": ")            
    return int(game_id), draws_string.split("; ")       # ex: 15, ["2 green", "3 red, 2 green", "2 red, 14 blue"]


def is_possible(drawn_set):                             # used in part 1, ex. input: 6 green, 1 blue, 3 red

    for cube_amount in drawn_set.split(", "):           # ex: 6 green

        value, color = cube_amount.split(" ")

        if colors[color] < int(value):
            return False
            
    return True


def part_one(task_input):

    result = 0

    for line in task_input:

        possible = True
        game_id, drawn_sets = parse_line(line)

        for drawn_set in drawn_sets:                    # ex: "3 red, 2 green"

            if not is_possible(drawn_set):
              
                possible = False
                break

        if possible:
            result += game_id

    return result


def part_two(task_input):
  
    result = 0
  
    for line in task_input:
      
        max_color_values = {"red": 0, "green": 0, "blue": 0}
        _, drawn_sets = parse_line(line)
      
        for drawn_set in drawn_sets:
          
            for cube_amount in drawn_set.split(", "):
              
                value, color = cube_amount.split(" ")
                max_color_values[color] = max(max_color_values[color], int(value))
              
        result += max_color_values["red"] * max_color_values["blue"] * max_color_values["green"]
      
    return result


print("Part one:", part_one(main_input))
print("Part two:", part_two(main_input))
