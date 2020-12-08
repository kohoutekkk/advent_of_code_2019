import copy
op_str = 'acc +7'


def parse_operation(operation_str):
    op_list = operation_str.strip().split()
    operation = op_list[0]
    op_sign = op_list[1][0]
    steps = op_list[1][1:]
    return {'operation': operation, 'sign': op_sign, 'steps': int(steps), 'visited': False}


# print(parse_operation(op_str))


#operations_file = open('data/test_operations.txt')
operations_file = open('data/operations.txt')

operations_original = [parse_operation(item) for item in operations_file.readlines()]
operations_file.close()


# print(operations_dicts[0])


def test_list(operations):
    one_outside = len(operations)
    acc = 0
    location = 0
    succ = False

    while 1 == 1:
        if location == one_outside:
            succ = True
            break
        if location > one_outside:
            #print('one_out_over')
            break
        if location < 0:
            #print('less than zero')
            break
        if operations[location]['visited'] == True:
            #print(location)
            #print(operations_dicts[location]['visited'])
            #print('cycle')
            break

        operations[location]['visited'] = True

        if operations[location]['operation'] == 'acc':
            if operations[location]['sign'] == '+':
                acc += operations[location]['steps']
            elif operations[location]['sign'] == '-':
                acc -= operations[location]['steps']
            #print(acc)

            location += 1

        elif operations[location]['operation'] == 'nop':
            location += 1

        elif operations[location]['operation'] == 'jmp':
            if operations[location]['sign'] == '+':
                location += operations[location]['steps']
            elif operations[location]['sign'] == '-':
                location -= operations[location]['steps']

    return acc, succ

ind = 0
success = False
while not success:
    #operations_file = open('data/operations.txt')
    #current_ops = [parse_operation(item) for item in operations_file.readlines()]
    #operations_file.close()
    current_ops = copy.deepcopy(operations_original)
    #print(id(current_ops))
    #print(id(operations_original))
    #print(operations_original[0]['operation'])

    #print(current_ops)
    if current_ops[ind]['operation'] == 'nop':
        current_ops[ind]['operation'] = 'jmp'
        accumulator, success = test_list(current_ops)
    elif current_ops[ind]['operation'] == 'jmp':
        current_ops[ind]['operation'] = 'nop'
        accumulator, success = test_list(current_ops)
    #print(current_ops)
    #print(ind, current_ops[ind]['operation'], accumulator, success)
    ind += 1

#print('-'* 100)

print(accumulator)
