def split_and_check(pw_input):
    counts, symbol, pw = pw_input.split(' ')
    symbol = symbol[:-1]
    lower_bound, upper_bound = counts.split('-')
    occurrence_count = pw.count(symbol)

    if int(lower_bound) <= occurrence_count <= int(upper_bound):
        return 1
    else:
        return 0

pw_file = open('data/pw_data.txt')
valid_pw_cnt = 0
for line in pw_file.readlines():
    valid_pw_cnt += split_and_check(line)

print(valid_pw_cnt)


