file = open("./day2/puzzleInput.txt")

AVAILABLE_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

result1 = 0
result2 = 0

for line in file:
    gameId, game = line.split(': ')
    gameId = int(gameId[5:])
    possible = True
    
    min_red = 0
    min_green = 0
    min_blue = 0

    for set in game.split('; '):

        for num_and_color in set.split(', '):
            num, color = num_and_color.split()
            num = int(num)

            # 1st part: check if a game is possible 
            if color == 'red' and num > AVAILABLE_CUBES['red']:
                possible = False
            elif color == 'green' and num > AVAILABLE_CUBES['green']:
                possible = False
            elif color == 'blue' and num > AVAILABLE_CUBES['blue']:
                possible = False


            # 2nd part: sum of power of the minimum cubes of every game
            if color == 'red' and num > min_red:
                min_red = num
            elif color == 'green' and num > min_green:
                min_green = num
            elif color == 'blue' and num > min_blue:
                min_blue = num

            
    if possible:
        result1 += gameId

    result2 += min_red * min_green * min_blue 


file.close()

print("1st part:", result1)
print("2nd part:", result2)