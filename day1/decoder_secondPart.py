valid_digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
result = 0

file = open("puzzleInput.txt")

def findFirst(line):
    first = False
    numberFound = ''

    
    
    return numberFound
        


def decodeNumber(line, word):
    resultString = ''

    match(word):
        case 'one':
            line.replace('one', '1')
        case 'two':
            line.replace('two', '2')
        case 'three':
            line.replace('three', '3')
        case 'four':
            line.replace('four', '4')
        case 'five':
            line.replace('five', '5')
        case 'six':
            line.replace('six', '6')
        case 'seven':
            line.replace('seven', '7')
        case 'eight':
            line.replace('eight', '8')
        case 'nine':
            line.replace('nine', '9')
        case _:
            resultString += word

    resultString = word
    
    return line



for line in file:
    resultString = ''
    array_line = []

    for word in valid_digit:
        if word in line:
            line = decodeNumber(line, word)
    

    print(line)

    #resultString += findFirst(line)
    #resultString += findFirst(line[::-1])

    

    #result += int(resultString)

file.close()

print(result)