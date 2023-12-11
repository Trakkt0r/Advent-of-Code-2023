from math import floor, ceil, sqrt

ERROR = 0.0001

with open("Day 6\input.txt", "r") as input_file:
    # tuple of (time, distance) pairs
    input_part1 = tuple(zip(*[map(lambda x: int(x), filter(str.isnumeric, line.strip("\n").split(" "))) for line in input_file]))

    # this approach is needed since you can't read the same file twice
    input_part2 = ["", ""]      
    for race in input_part1:
        input_part2[0] += str(race[0])
        input_part2[1] += str(race[1])

    input_part2 = ((int(input_part2[0]), int(input_part2[1])),)


def quadratic(a, b, c):                         # only returns real values

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None

    rooted_discriminant = sqrt(discriminant)

    return (-b - rooted_discriminant)/2*a, (-b + rooted_discriminant)/2*a


def main(races):
    
    product = 1

    for race in races:

        time, distance = race
        root_discriminant = sqrt(time**2 - 4*distance)      # too expensive to compute twice
        min_windtime, max_windtime = [(time + sign*root_discriminant) / 2 for sign in (-1, 1)]

        product *= floor(max_windtime-ERROR) - ceil(min_windtime+ERROR) + 1 

    return product


print(main(input_part1))
print(main(input_part2))
