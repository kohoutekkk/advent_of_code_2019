trees_file = open('data/trees.txt')
#trees_file = open('data/test_tree.txt')
forest = trees_file.readlines()
trees_file.close()

clean_forest = [tree_row.strip() for tree_row in forest]

right = 3
down = 1
rows = len(clean_forest)
cols = len(clean_forest[0])


def jump(right, down, step, cols):
    return (right*step) % cols, down*step

# you begin in [0,0]
def calc_trees(right, down, cols):
    trees_in_path = 0
    for step in range(1,(rows//down)):
        col, row = jump(right,down,step,cols)
        trees_in_path += 1 if clean_forest[row][col] == '#' else 0
    return trees_in_path

diagonals = [(1,1),(3,1),(5,1),(7,1),(1,2)]

product = 1
for diagonal in diagonals:
    product *= calc_trees(diagonal[0], diagonal[1], cols)

print(product)
