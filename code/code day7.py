CARD_ORDER = []

def part1(hands):
    global CARD_ORDER
    CARD_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    hand_types = {'five':[],'four':[],'full':[],'three':[],'twopair':[],'pair':[],'none':[]}
    handsonly = [i[0] for i in hands]

    # sort each hand into its hand types
    for hand in hands:

        # get number of similar chars
        values = {}
        for card in [*hand[0]]:
            if card in values:
                values[card] += 1
            else:
                values[card] = 1

        # sort by type of hand into whole list
        sortedvalues = sorted(list(values.values()))
        sortedvalues.reverse()
        if 5 in sortedvalues:
            hand_types['five'].append(hand[0])
        elif 4 in sortedvalues:
            hand_types['four'].append(hand[0])
        elif 3 in sortedvalues and 2 in sortedvalues:
            hand_types['full'].append(hand[0])
        elif 3 in sortedvalues:
            hand_types['three'].append(hand[0])
        elif 2 in sortedvalues:
            if len([i for i in sortedvalues if i == 2]) == 2:
                hand_types['twopair'].append(hand[0])
            else:
                hand_types['pair'].append(hand[0])
        else:
            hand_types['none'].append(hand[0])
    
    # sort each hand type
    hand_types_new = {'five':[],'four':[],'full':[],'three':[],'twopair':[],'pair':[],'none':[]}
    for hand_type in hand_types:
        sorted_hands = sorted(hand_types[hand_type], key=sort_function)
        hand_types_new[hand_type] = sorted_hands

    hands_ordered = []
    for hand_type in hand_types_new:
        hands_ordered.extend(hand_types_new[hand_type])
    hands_ordered.reverse()

    # tally bids multiplied by rank
    total = 0
    for hand in hands_ordered:
        total += (int(hands[handsonly.index(hand)][1])) * (hands_ordered.index(hand)+1)
    
    return total
          

def sort_function(c):
    global CARD_ORDER
    count = 0
    listofchars = [*c]
    listofchars.reverse()
    cindex = 1
    for i in listofchars:
        count += CARD_ORDER.index(i)*(100**cindex)
        cindex += 1
    return count

def part2(hands):
    global CARD_ORDER
    CARD_ORDER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    hand_types = {'five':[],'four':[],'full':[],'three':[],'twopair':[],'pair':[],'none':[]}
    handsonly = [i[0] for i in hands]
    for hand in hands:
        allhands = []
        for i in range(0, 6):
            allhands.extend([hand[0].replace("J", j, i) for j in CARD_ORDER])
        sortedhands = sorted(allhands, key=sort_function_2)
        values = {}
        for card in [*sortedhands[-1]]:
            if card in values:
                values[card] += 1
            else:
                values[card] = 1
        sortedvalues = sorted(list(values.values()))
        sortedvalues.reverse()
        if 5 in sortedvalues:
            hand_types['five'].append(hand[0])
        elif 4 in sortedvalues:
            hand_types['four'].append(hand[0])
        elif 3 in sortedvalues and 2 in sortedvalues:
            hand_types['full'].append(hand[0])
        elif 3 in sortedvalues:
            hand_types['three'].append(hand[0])
        elif 2 in sortedvalues:
            if len([i for i in sortedvalues if i == 2]) == 2:
                hand_types['twopair'].append(hand[0])
            else:
                hand_types['pair'].append(hand[0])
        else:
            hand_types['none'].append(hand[0])
    
    hand_types_new = {'five':[],'four':[],'full':[],'three':[],'twopair':[],'pair':[],'none':[]}
    for hand_type in hand_types:
        sorted_hands = sorted(hand_types[hand_type], key=sort_function)
        hand_types_new[hand_type] = sorted_hands

    hands_ordered = []
    for hand_type in hand_types_new:
        hands_ordered.extend(hand_types_new[hand_type])
    hands_ordered.reverse()
    total = 0
    for hand in hands_ordered:
        total += (int(hands[handsonly.index(hand)][1])) * (hands_ordered.index(hand)+1)
    return total

def sort_function_2(hand):
    values = {}
    for card in [*hand]:
        if card in values:
            values[card] += 1
        else:
            values[card] = 1
    sortedvalues = sorted(list(values.values()))
    sortedvalues.reverse()
    
    if 5 in sortedvalues:
        return 6
    elif 4 in sortedvalues:
        return 5
    elif 3 in sortedvalues and 2 in sortedvalues:
        return 4
    elif 3 in sortedvalues:
        return 3
    elif 2 in sortedvalues:
        if len([i for i in sortedvalues if i == 2]) == 2:
            return 2
        else:
            return 1
    else:
        return 0


with open("tests/input day7.txt", "r") as file:
    hands = [i.split() for i in file]


print(part1(hands))
print(part2(hands))
    