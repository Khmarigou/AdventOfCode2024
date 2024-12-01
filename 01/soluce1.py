def diff(a, b) :
    return abs(a - b)

def getInput(file):
    left = []
    right = []
    with open(file, "r") as f:
        for line in f:
            split = line.split()
            left.append(int(split[0]))
            right.append(int(split[1]))
    left.sort()
    right.sort()
    return left, right

if __name__ == '__main__':
    result = 0
    left, right = getInput("input.txt")
    if (len(left) != len(right)):
        print("Error: left and right are not the same size")
        exit(1)
    else :
        for i in range(len(left)):
            result += diff(left[i], right[i])
        print(result)