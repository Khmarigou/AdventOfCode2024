from soluce1 import isValid

def main() :
    result = 0
    with open("input.txt", "r") as f:
        for line in f :
            levels = line.split()
            if not isValid(levels) :
                for i in range(len(levels)) :
                    newLevels = levels.copy()
                    newLevels.pop(i)
                    if isValid(newLevels) :
                        result += 1
                        break
            else :
                result += 1
    print(result)

if __name__ == '__main__':
    main()