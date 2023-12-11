winnings = {
    'red': 12,
    'green': 13,
    'blue': 14
}
sum = 0

file = 'puzzle.txt'
with open(file) as f:
    for line in f:
        game = line.strip().split(':')
        cubes = game[1].split(';')
        game_id = int(game[0].strip().split()[1])
        c_game = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for move in cubes:
            pieces = move.strip().split(',')
            for piece in pieces:
                count = int(piece.strip().split()[0])
                color = piece.strip().split()[1]
                if count > c_game[color]:
                    c_game[color] = count

        if all(c_game[color] <= winnings[color] for color in winnings):
            sum += game_id

print(sum)
