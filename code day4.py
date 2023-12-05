with open("input day4.txt", "r") as file:data = [i for i in file]

def part1():
    total = 0
    for card in data:
        cardno, cardinfo = card.split(":")
        winning, current = cardinfo.split("|")
        winning = winning.split()
        current = current.split()
        matches = len([key for key, val in enumerate(current) if val in set(winning)])
        value = 2**(matches-1)
        total = total + value if value >= 1 else total + 0
    print(f"part 1: {total}")

def part2():
    global data
    cardswon = [str(i+1) for i in range(len(data))]
    for card in data:
        cardno, cardinfo = card.split(":")
        winning, current = cardinfo.split("|")
        _, cardnumber = cardno.split()
        if cardnumber not in cardswon:
            break
        winning = winning.split()
        current = current.split()
        matches = len([key for key, val in enumerate(current) if val in set(winning)])
        for i in range(cardswon.count(cardnumber)):
            for j in range(matches):
                cardswon.append(str(int(cardnumber)+j+1))
    print(f"part 2: {len(cardswon)}")

def faster_part2():
    cardswon = {str(i+1):1 for i in range(len(data))}
    for card in data:
        cardswon={j:(cardswon[j]+(1*cardswon[card.split(":")[0].split()[1]]) if j in [str(i+1+int(card.split(":")[0].split()[1])) for i in range(len([key for key, val in enumerate(card.split(":")[1].split("|")[1].split()) if val in set(card.split(":")[1].split("|")[0].split())]))] else cardswon[j]) for j in cardswon}
    print(f"part 2: {sum(cardswon.values())}")

part1()
faster_part2()
