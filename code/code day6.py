import math

def quad_formula(a, b, c):
    sol1 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
    sol2 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
    sol1 = math.ceil(sol1) if not sol1.is_integer() else sol1+1
    sol2 = math.floor(sol2) if not sol2.is_integer() else sol2-1
    return int(sol1), int(sol2)

def part1(times, distances):
    total = 1
    for time, distance in zip(times, distances):
        total *= part2(time, distance)
    return total

def part2(time, distance):
    solutions = quad_formula(1, -time, distance)
    rangelen = len(range(solutions[0], solutions[1]+1))
    return rangelen

with open("tests/input day6.txt", "r") as file:
    times, distances = [[int(i.strip()) for i in i.split(":")[1].split()] for i in file]
    time, distance = int("".join([str(i) for i in times])), int("".join([str(i) for i in distances]))

print(f"Part 1: {part1(times, distances)}")
print(f"Part 1: {part2(time, distance)}")


