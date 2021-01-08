import numpy as np

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


x_min = 0
x_max = 0
y_min = 0
y_max = 0

for row in tile_file.readlines():
    flip = find_final(row.strip())

    x_min = min(x_min, flip[0])
    x_max = max(x_max, flip[0])
    y_min = min(y_min, flip[1])
    y_max = max(y_max, flip[1])

    # print(flip)
    if flip in tiles:
        tiles.remove(flip)
    else:
        tiles.add(flip)

print(len(tiles))

print(tiles)

# print(find_final(row))

# {(-1, 1), (0, 0), (-4, -2), (-3, -3), (-3, -1), (3, 3), (2, -2), (-3, 1), (-4, 0), (4, 0)}

s_x_0 = x_max - x_min + 4
s_y_0 = y_max - y_min + 4

s_x = s_x_0 + 4 if s_x_0 % 2 == 0 else s_x_0 + 5
s_y = s_y_0 + 4 if s_y_0 % 2 == 0 else s_y_0 + 5

print(y_max, y_min)

zero_field_x = s_x // 2 if (s_x // 2) % 2 == 0 else s_x // 2 + 1
zero_field_y = s_y // 2 if (s_y // 2) % 2 == 0 else s_y // 2 + 1

print(s_x, s_y, zero_field_x, zero_field_y)

# problem is like conway, but there is a catch. with hex neighbors. if we start at field [0,0]
# we can only get to fields with even sum of coordinates [1,1] [2,0]..
# by correctly initiating the first array, we can then skip over all fields, that do not have such coords
# and work in 2d array with neighbours manhattan distance 2 away e.g [4,4] check neighbours, [3,4] do not

original_field = np.zeros([s_x, s_y])

for tile in tiles:
    original_field[zero_field_x + tile[0], zero_field_y + tile[1]] = 1

print(original_field)


def get_next_gen(original_field):
    neighbors = [(-1, -1), (1, -1), (2, 0), (1, 1), (-1, 1), (-2, 0)]
    original_field = np.pad(original_field, (2, 2), 'constant')
    next_field = original_field.copy()

    for i in range(original_field.shape[0]):
        for j in range(original_field.shape[1]):
            coord_sum = i + j
            cs2 = coord_sum % 2
            if cs2 == 0:
                blacks = 0
                for neighbor in neighbors:
                    try:
                        blacks += original_field[i + neighbor[0], j + neighbor[1]]
                    except:
                        blacks += 0

                if original_field[i,j] == 1 and (blacks == 0 or blacks > 2):
                    next_field[i,j] = 0

                if original_field[i,j] == 0 and blacks == 2:
                    next_field[i,j] = 1

    return next_field

#nf = get_next_gen(original_field)
#print(sum(sum(nf)))

for iteration in range(100):
    original_field = get_next_gen(original_field)
    print(f'in step {iteration + 1} there was: {sum(sum(original_field))}  black tiles')

