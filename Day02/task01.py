w_red = 12
w_green = 13
w_blue = 14

sum = 0

file = 'puzzle.txt'
with open(file) as f:
    for line in f:
        game = line.strip().split(':')
        cubes = game[1].split(';')
        game_id = int(game[0].strip().split()[1])
        red = 0
        green = 0
        blue = 0

        for move in cubes:
            pieces = move.strip().split(',')
            for piece in pieces:
                count = int(piece.strip().split()[0])
                color = piece.strip().split()[1]
                if color == 'red' and count > red:
                    red = count
                if color == 'green' and count > green:
                    green = count
                if color == 'blue' and count > blue:
                    blue = count

        if red <= w_red and green <= w_green and blue <= w_blue:
            sum += game_id

print(sum)
