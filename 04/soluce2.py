from soluce1 import getInput

def checkX(grid, x, y) :
    if x >= 1 and y >= 1 and x < len(grid[y]) - 1 and y < len(grid) - 1 :
        # UP
        if grid[y-1][x-1] == "M" and grid[y-1][x+1] == "M" and grid[y+1][x-1] == "S" and grid[y+1][x+1] == "S" :
            return 1
        # DOWN
        elif grid[y+1][x-1] == "M" and grid[y+1][x+1] == "M" and grid[y-1][x-1] == "S" and grid[y-1][x+1] == "S" :
            return 1
        # RIGHT
        elif grid[y-1][x+1] == "M" and grid[y+1][x+1] == "M" and grid[y-1][x-1] == "S" and grid[y+1][x-1] == "S" :
            return 1
        # LEFT
        elif grid[y-1][x-1] == "M" and grid[y+1][x-1] == "M" and grid[y-1][x+1] == "S" and grid[y+1][x+1] == "S" :
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
            if input[y][x] == 'A' :
                result += checkX(input, x, y)
    print(result)

if __name__ == '__main__' :
    main()