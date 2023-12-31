
def isFirstWordDigit(inp):
    #if inp[0:3] == "zero":
    #    return 0
    if inp[:3] == "one":
        return 1
    elif inp[:3] == "two":
        return 2
    elif inp[:5] == "three":
        return 3
    elif inp[:4] == "four":
        return 4
    elif inp[:4] == "five":
        return 5
    elif inp[:3] == "six":
        return 6
    elif inp[:5] == "seven":
        return 7
    elif inp[:5] == "eight":
        return 8
    elif inp[:4] == "nine":
        return 9
    else:
        return 0


def isSecondWordDigit(inp):
    #if inp[0:3] == "zero":
    #    return 0
    #print(inp[-5:])
    if inp[-3:] == "one":
        return 1
    elif inp[-3:] == "two":
        return 2
    elif inp[-5:] == "three":
        return 3
    elif inp[-4:] == "four":
        return 4
    elif inp[-4:] == "five":
        return 5
    elif inp[-3:] == "six":
        return 6
    elif inp[-5:] == "seven":
        return 7
    elif inp[-5:] == "eight":
        return 8
    elif inp[-4:] == "nine":
        return 9
    else:
        return 0


File_object = open(r"./AoC/Inp01.txt", "r")
lines = File_object.readlines()

sum = 0
for line in lines:
    n = len(line)
    r = range(0,n)
    for i in r:
        if line[i].isdigit():
            first = line[i]
            break
        elif isFirstWordDigit(line[i:]) != 0:
            first = isFirstWordDigit(line[i:])
            break
    for i in r:
        if line[n-i-1].isdigit():
            second = line[n-i-1]
            break
        elif isSecondWordDigit(line[:-i-1]) != 0:
            second = isSecondWordDigit(line[:-i-1])
            break
    print(line, first, second)
    sum += 10*int(first) + int(second)

print(sum)
