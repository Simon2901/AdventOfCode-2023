with open('day1/input.txt') as f:
    lines = f.readlines()

number_words = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

res = 0
for line in lines:
    num = []
    for number in number_words:
        line = line.replace(number, number_words[number])
    for i in range(len(line)):
        if ord(line[i]) in range(ord("0"), ord("9") + 1):
            num.append(line[i])
    res += int("".join([str(num[i]) for i in (0, -1)]))
    
print(res)