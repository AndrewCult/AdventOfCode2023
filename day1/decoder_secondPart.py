valid_digit = {
    'one': 1, 
    'two': 2,
    'three': 3,
    'four': 4, 
    'five': 5,
    'six': 6, 
    'seven': 7,
    'eight': 8,
    'nine': 9
}

result = 0

file = open("puzzleInput.txt")

def checkDigit(line):
    if line[0].isdigit():
        return int(line[0])
    
    # check if inside string line (in puzzleInput.txt) is present a number written in letter (stored in valid_digit), if not return None. 
    wordNumber = next(filter(line.startswith, valid_digit), None)
    return valid_digit.get(wordNumber, 0)


for line in file:

    for i in range(len(line)):
        first = checkDigit(line[i:])
        if first:
            break

    for i in range(len(line) - 1, -1, -1):
        last = checkDigit(line[i:])
        if last:
            break

    result += 10*first + last

file.close()

print(result)