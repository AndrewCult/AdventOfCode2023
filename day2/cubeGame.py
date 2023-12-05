file = open("puzzleInput.txt")

AVAILABLE_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

result1 = 0

for line in file:
    gameId, game = line.split(': ')
    gameId = int(gameId[5:])
    possible = True
    
    for set in game.split('; '):
        for num_and_color in set.split(', '):
            num, color = num_and_color.split()
            num = int(num)

            if color == 'red' and num > AVAILABLE_CUBES['red']:
                possible = False
            elif color == 'green' and num > AVAILABLE_CUBES['green']:
                possible = False
            elif color == 'blue' and num > AVAILABLE_CUBES['blue']:
                possible = False
            
    if possible:
        result1 += gameId


file.close()

print("First part:", result1)