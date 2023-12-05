with open("tests/input day1.txt", "r") as file:
    data = [i for i in file]
nums = {'one':1, 'two':2, 'three':3, 'four': 4, 'five':5, 'six':6, "seven":7, 'eight':8, 'nine':9, 'zero':0}

total = 0
for i in data:
    first = None
    last = None
    word = ""
    for j in [*i]:
        if j.isdigit(): # part one solution to find all digits
            last = j
            if first == None:
                first = j
        else: # part 2 solution, adds letters to a word untill it spells a number, then 'clears' it
            word+=j
            for i in nums:
                if i in word:
                    number = str(nums[i])
                    word = word[-1] # account for stuff like twone
                    last = number
                    if first == None:
                        first = number
    wholenum = int(first+last)
    total += wholenum
print(total)

