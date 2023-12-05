def parse(line):
    game, games = line.split(":")
    gameid = game.split()[1]
    gameesarray = games.split(";")
    colordict = {'red':0, 'blue':0, 'green':0}

    for i in gameesarray:
        splitarray = i.split(",")
        for i in splitarray:
            color = i.split()[1]
            score = i.split()[0]
            if colordict[color] < int(score):
                colordict[color] = int(score)
    return colordict, int(gameid)

with open("tests/input day2.txt", "r") as file: data = [i for i in file]
countvalidgameid = 0
countpowers = 0

for i in data:
    # part 1
    parsedcolors, gameid = parse(i)
    if not ((parsedcolors["red"]>12) or (parsedcolors["green"]>13) or (parsedcolors["blue"]>14)):
        countvalidgameid += gameid

    # part 2
    power = parsedcolors["red"] * parsedcolors["green"] * parsedcolors["blue"] 
    countpowers += power
    
print(f"First: {countvalidgameid}, Second: {countpowers}")




