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

res = 0

for line in lines:
    num = []
    i = 0
    while i < len(line):
        if ord(line[i]) in range(ord("0"), ord("9") + 1):
            num.append(line[i])
            i += 1
        else:
            for j in range(3,5+1):
                if line[i:min(i+j, len(line)-1)] in number_words:
                    num.append(str(number_words[line[i:min(i+j, len(line)-1)]]))
                    break
            i += 1
        
    res += int("".join([str(num[i]) for i in (0, -1)]))

print(res)