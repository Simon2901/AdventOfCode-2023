# Data Preprocessing
with open('day2/input.txt') as f:
  lines = f.readlines()
  games = {}
  
  for line in lines:
    line = line.strip()
    game = line.split(":")
    rounds = [[items.strip().split(" ") for items in round.split(",")] for round in game[1].split(";")]
    games[game[0]] = rounds
    
## Task 1
bag = {
  "red": 12,
  "green": 13,
  "blue": 14
}

# check games
print(games.keys())
valid = [True]*len(games)
for i, game in enumerate(games.values()):
  for round in game:
    for item in round:
      print(item)
      if item[1] in bag and int(item[0]) > bag[item[1]]:
        valid[i] = False

# calc sum of valid games
sumValidGames = sum([int(g.split(" ")[1]) * v for g, v in zip(games.keys(), valid)])

print(sumValidGames)

## Task 2
powers = []

def prod(list: list) -> int:
  res = 1
  for e in list:
    res *= e
  return res

for game in games.values():
  
  bag = {
    "red": 0,
    "green": 0,
    "blue": 0
  }
  
  # get minim count of cubes per color
  for round in game:
    for item in round:
      if int(item[0]) > bag[item[1]]:
        bag[item[1]] = int(item[0])
  
  # calc power
  powers.append(prod(bag.values()))

# calc sum of powers
sumPowers = sum(powers)

print(sumPowers)
  
