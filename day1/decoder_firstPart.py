file = open("puzzleInput.txt")
result = 0


def findFirst(line):
    first = False
    numberFound = ''

    for n in line:
        if n.isdigit() and first == False:
            first = True
            numberFound = n
    
    return numberFound


for line in file:
    resultString = ''
    resultString += findFirst(line)
    resultString += findFirst(line[::-1])

    result += int(resultString)

file.close()

print(result)