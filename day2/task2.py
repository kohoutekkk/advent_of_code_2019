def split_and_check(pw_input):
    positions, symbol, pw = pw_input.split(' ')
    symbol = symbol[:-1]
    first_position, second_position = positions.split('-')
    python_first_position = int(first_position) - 1
    python_second_position = int(second_position) - 1
    matches = (pw[python_first_position] == symbol) + (pw[python_second_position] == symbol)

    if matches == 1:
        return True
    else:
        return False

#in_str = '2-9 c: ccccccccc'
#print(split_and_check(in_str))

pw_file = open('data/pw_data.txt')
valid_pw_cnt = 0
for line in pw_file.readlines():
    valid_pw_cnt += split_and_check(line)

print(valid_pw_cnt)


