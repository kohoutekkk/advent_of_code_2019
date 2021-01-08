#tile_file = open('data/test_in.txt')
tile_file = open('data/in.txt')

# hexagonal tiles can be still managed with 2d field move east is move [2,0] and move se [-1,1] etc.
# that way each tile has exact coordinates

row = 'esenee'

tiles = set()


def find_final(row):
    c1 = 0
    c2 = 0
    s_move = False
    n_move = False
    for letter in row:

        if letter == 's':
            s_move = True

        if letter == 'n':
            n_move = True
        if letter == 'e':
            if s_move:
                s_move = False
                c1 += 1
                c2 += -1

            elif n_move:
                n_move = False
                c1 += 1
                c2 += 1

            else:
                c1 += 2

        if letter == 'w':
            if s_move:
                s_move = False
                c1 += -1
                c2 += -1

            elif n_move:
                n_move = False
                c1 += -1
                c2 += 1

            else:
                c1 += -2

        # print(c1,c2)

    return (c1, c2)


for row in tile_file.readlines():
    flip = find_final(row.strip())
    #print(flip)
    if flip in tiles:
        tiles.remove(flip)
    else:
        tiles.add(flip)

print(len(tiles))

# print(find_final(row))
