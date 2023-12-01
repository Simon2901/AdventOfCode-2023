with open('day1/input.txt') as f:
    lines = f.readlines()

number_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

number_words_backw = dict([(x[::-1], y) for x, y in number_words.items()])

def get_First(line):
    for i in range(len(line)):
        for j in range(3,5+1):
            if line[i:i+j] in number_words:
                line = line[0:i] + str(number_words[line[i:i+j]]) + line[i+j:]
                return line
    return line

def get_Last(line):
    for i in range(len(line)-1,-1,-1):
        for j in range(3,5+1):
            if line[i:i-j:-1] in number_words_backw:
                line = line[0:i-j+1] + str(number_words_backw[line[i:i-j:-1]]) + line[i+1:]
                return line
    return line

res = 0
for line in lines:
    line = get_Last(get_First(line))
    
    print(line)
    num=[]
    for i in range(len(line)):
        if ord(line[i]) in range(ord("0"), ord("9") + 1):
            num.append(line[i])
    res += int("".join([str(num[i]) for i in (0, -1)]))
    
print("result",res)