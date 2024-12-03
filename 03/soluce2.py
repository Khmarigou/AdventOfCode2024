import re

def main() :
    result = 0
    with open('input.txt', 'r') as f :
        p = re.compile('mul\((\d+),(\d+)\)')
        line = f.read()
        spl = line.split("do()")
        for s in spl :
            doing = s[:s.index("don't()")] if "don't()" in s else s
            matches = p.findall(doing)
            for m in matches :
                result += int(m[0]) * int(m[1])
    print(result)

if __name__ == '__main__' :
    main()