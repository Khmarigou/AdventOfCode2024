def getInput(file) :
    input = []
    with open(file, "r") as f :
        for line in f :
            input.append(line)
    return input

def checkR(grid, x, y) :
    if x < len(grid[y]) - 3 :
        word = grid[y][x:x+4]
        if word == "XMAS" :
            return 1
        else :
            return 0
    else :
        return 0
    
def checkL(grid, x, y) :
    if x >= 3 :
        word = grid[y][x-3:x+1]
        if word == "SAMX" :
            return 1
        else :
            return 0
    else :
        return 0

def checkU(grid, x, y) :
    if y >= 3 :
        word = ""
        for i in range(4) :
            word += grid[y - i][x]
        if word == "XMAS" :
            return 1
        else :
            return 0
    else :
        return 0
    
def checkD(grid, x, y) :
    if y < len(grid) - 3 :
        word = ""
        for i in range(4) :
            word += grid[y + i][x]
        if word == "XMAS" :
            return 1
        else :
            return 0
    else :
        return 0

def checkRU(grid, x, y) :
    if y >= 3  and x < len(grid[y]) - 3 :
        word = ""
        for i in range(4) :
            word += grid[y - i][x + i]
        if word == "XMAS" :
            return 1
        else :
            return 0
    else :
        return 0
    
def checkRD(grid, x, y) :
    if y < len(grid) - 3  and x < len(grid[y]) - 3 :
        word = ""
        for i in range(4) :
            word += grid[y + i][x + i]
        if word == "XMAS" :
            return 1
        else :
            return 0
    else :
        return 0

def checkLU(grid, x, y) :
    if y >= 3  and x >= 3 :
        word = ""
        for i in range(4) :
            word += grid[y - i][x - i]
        if word == "XMAS" :
            return 1
        else :
            return 0
    else :
        return 0

def checkLD(grid, x, y) :
    if y < len(grid) - 3  and x >= 3 :
        word = ""
        for i in range(4) :
            word += grid[y + i][x - i]
        if word == "XMAS" :
            return 1
        else :
            return 0
    else :
        return 0

def main() :
    input = getInput("input.txt")
    result = 0
    for y in range(len(input)) :
        for x in range(len(input[y])) :
            if input[y][x] == 'X' :
                result += checkR(input, x, y)
                result += checkL(input, x, y)
                result += checkU(input, x, y)
                result += checkD(input, x, y)
                result += checkRU(input, x, y)
                result += checkRD(input, x, y)
                result += checkLU(input, x, y)
                result += checkLD(input, x, y)
    print(result)

if __name__ == '__main__' :
    main()