import re

def main() :
    result = 0
    with open('input.txt', 'r') as f :
        for line in f :
            matches = re.findall('mul\((\d+),(\d+)\)', line)
            for m in matches :
                result += int(m[0]) * int(m[1])
    print(result)


if __name__ == '__main__' :
    main()