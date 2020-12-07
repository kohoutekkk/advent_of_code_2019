#bags = open('data/test_bags.txt')
bags = open('data/bags.txt')

#bags_list = [bag for bag in bags.readlines()]


def contained_bag_proc(bg):
    #print(bg)
    plain_bg = bg.strip()
    cnt = int(plain_bg.split()[0])
    bag_col = ' '.join(plain_bg.split()[1:-1])
    return bag_col, cnt


def parse_bag(bag):
    main_and_cont = bag.split('contain')
    main_bag = main_and_cont[0].strip()[:-5]

    cont_part = main_and_cont[1].strip()
    if cont_part == 'no other bags.':
        contained_bags = {}
    else:
        #remove the dot and separate into same parts per bag contained
        contained_bags = cont_part[:-1].split(',')
        contained_bags = {contained_bag_proc(cb)[0]: contained_bag_proc(cb)[1] for cb in contained_bags}
     #   print(contained_bags)
    #print(main_bag)
    return main_bag, contained_bags


bags_list = [parse_bag(bag) for bag in bags.readlines()]
bags_dict = {key:value for key,value in bags_list}

#for bag in bags_list:
#    print(bag)

#print(bags_dict)
my_bag = 'shiny gold'

def recursive_search(col):
    col_list = []
    core_cols = list(bags_dict[col].keys())
    while core_cols:
        contained_col = core_cols.pop()
        if contained_col not in col_list:
            col_list.append(contained_col)
            core_cols += list(bags_dict[contained_col].keys())
    #return col_list
    if my_bag in col_list:
        return 1
    else:
        return 0

total = 0
for color in list(bags_dict.keys()):
    total += recursive_search(color)
#print(list(bags_dict.keys())[0], recursive_search(list(bags_dict.keys())[0]))
print(total)