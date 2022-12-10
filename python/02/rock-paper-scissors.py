input = open("input.txt", "r")
lines = [line.strip() for line in input.readlines()]
# part 1
choiceMap = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

["X", "Y", "Z"]
["B", "C", "A"]

score = sum([choiceMap[round] for round in lines])
print(score)
# part 2
outcomeMap = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7   
}

score = sum([outcomeMap[round] for round in lines])
print(score)
