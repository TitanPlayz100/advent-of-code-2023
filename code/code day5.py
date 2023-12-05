def getPosInList(listinput, item, nth_item_num):
    count = 0
    positions = [i for i in range(len(listinput)) if listinput[i] == item]
    return positions[nth_item_num-1] if nth_item_num-1 < len(positions) else None

def findLowestNum(maps_dict, seed):
    next_word = list(maps_dict.keys())[0].split("-")[0]
    number_to_translate = int(seed)
    while next_word != 'location':
        for map_type in maps_dict.keys():
            if next_word == map_type.split("-")[0]:
                next_word = map_type.split("-")[2]
                number_to_translate = translateNumber(number_to_translate, maps_dict[map_type])
    return number_to_translate

def translateNumber(number, valueList):
    for value in valueList:
        des_range, src_range, length = value.split()
        if number in range(int(src_range), int(src_range)+int(length)):
            new_number = number + (int(des_range)-int(src_range))
            return new_number
    return number
    
def part_1(data):
    seeds = data[0].split(":")[1].split()
    maps_dict = {}
    for index in range(len(data)):
        if "map" in data[index]:
            mapname = data[index].split(":")[0].split()[0]
            mapdata = [j for j in data[index+1:getPosInList(data, "", len(maps_dict)+2):]]
            maps_dict[mapname] = mapdata
    
    lowest_num = None
    for seed in seeds:
        lowest_num_found = findLowestNum(maps_dict, seed)
        lowest_num = lowest_num_found if lowest_num == None else lowest_num
        lowest_num = lowest_num_found if lowest_num_found < lowest_num else lowest_num
    return lowest_num

def part_2(filename): # could not do
    seeds, *maps = open(filename).read().split('\n\n')
    seeds = [int(i) for i in seeds.split()[1:]]
    maps = [[[int(i) for i in line.split()] for line in m.splitlines()[1:]] for m in maps]
    ranges = list(zip(seeds[::2], seeds[1::2]))
    for m in maps:
        new_ranges = []
        for rs, rl in ranges:
            for md, ms, ml in m:
                if rs < ms + ml and ms < rs + rl:
                    os = max(rs, ms)
                    ol = min(rs + rl, ms + ml) - os
                    new_ranges += [(os - ms + md, ol)]
                    if os > rs: ranges += [(rs, os - rs)]
                    if os + ol < rs + rl: ranges += [(os + ol, rs + rl - os - ol)]
                    break
            else: new_ranges += [(rs, rl)]
        ranges = new_ranges
    return min(r for r, _ in ranges)

with open("tests/input day5.txt", "r") as file:
    data = [i.strip() for i in file]

print(f"Part 1: {part_1(data)}")
part2ans = part_2("tests/input day5.txt")
print(f"Part 2: {part2ans}")




