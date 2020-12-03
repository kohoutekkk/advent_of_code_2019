trees_file = open('data/trees.txt')
forest = trees_file.readlines()
trees_file.close()

clean_forest = [tree_row.strip() for tree_row in forest]

right = 3
down = 1
rows = len(clean_forest)
cols = len(clean_forest[0])


def jump(right, down, step, cols):
    return (right*step) % cols, down*step

# jou begin in [0,0]
trees_in_path = 0
for step in range(1,(rows//down)):
    col, row = jump(right,down,step,cols)
    #print(col, row, rows, clean_forest[row][col], cols, step)
    #print(clean_forest[row])
    trees_in_path += 1 if clean_forest[row][col] == '#' else 0

print(trees_in_path)