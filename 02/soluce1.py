def maxIncr(levels) :
    maxi = 0
    for i in range(len(levels) - 1) :
        maxi = max(maxi, abs(int(levels[i]) - int(levels[i + 1])))
    return maxi
    
def isDecrease(levels) :
    result = True
    for i in range(len(levels) - 1) :
        if (int(levels[i]) - int(levels[i + 1])) <= 0 :
            result = False
            break
    return result

def isIncrease(levels) :
    result = True
    for i in range(len(levels) - 1) :
        if (int(levels[i]) - int(levels[i + 1])) >= 0 :
            result = False
            break
    return result

def isValid(levels) :
    return maxIncr(levels) <= 3 and (isDecrease(levels) or isIncrease(levels))

def main() :
    result = 0
    with open("input.txt", "r") as f:
        for line in f :
            levels = line.split()
            if isValid(levels) :
                result += 1
    print(result)

if __name__ == '__main__':
    main()