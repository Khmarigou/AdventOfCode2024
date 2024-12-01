def getInput(filename):
    left = []
    right = []
    with open(filename, "r") as f:
        for line in f:
            split = line.split()
            left.append(int(split[0]))
            right.append(int(split[1]))
    return left, right


def main() :
    result = 0
    left, right = getInput("input.txt")
    occur = {}
    for n in left :
        if n in right and n not in occur:
            occur[n] = right.count(n)
        elif n in right and n in occur:
            occur[n] += right.count(n)
    for n in occur :
        result += (occur[n] * n)
    print(result)

if __name__ == '__main__':
    main()