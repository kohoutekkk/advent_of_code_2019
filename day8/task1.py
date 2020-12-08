
op_str = 'acc +7'

def parse_operation(operation_str):
    op_list = operation_str.strip().split()
    operation = op_list[0]
    op_sign = op_list[1][0]
    steps = op_list[1][1:]
    return {'operation': operation, 'sign': op_sign, 'steps': int(steps), 'visited': False}
#print(parse_operation(op_str))


#operations_file = open('data/test_operations.txt')
operations_file = open('data/operations.txt')

operations_dicts = [parse_operation(item) for item in operations_file.readlines()]
operations_file.close()

#print(operations_dicts[0])

accumulator = 0
location = 0
cycle = False

while 1 == 1:
    if operations_dicts[location]['visited']:
        break

    operations_dicts[location]['visited'] = True

    if operations_dicts[location]['operation'] == 'acc':
        if operations_dicts[location]['sign'] == '+':
            accumulator += operations_dicts[location]['steps']
        elif operations_dicts[location]['sign'] == '-':
            accumulator -= operations_dicts[location]['steps']

        location += 1

    elif operations_dicts[location]['operation'] == 'nop':
        location += 1

    elif operations_dicts[location]['operation'] == 'jmp':
        if operations_dicts[location]['sign'] == '+':
            location += operations_dicts[location]['steps']
        elif operations_dicts[location]['sign'] == '-':
            location -= operations_dicts[location]['steps']

print(accumulator)




