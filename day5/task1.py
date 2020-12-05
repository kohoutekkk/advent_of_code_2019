# bp = 'BFFFBBFRRR'
passes = open('data/boarding_passes.txt', 'r')


# passes = open('data/boarding_passes_test.txt', 'r)


def convert_to_bin(instr, one, zero):
    return int(instr.replace(one, '1').replace(zero, '0'), 2)


def seat_desc(bp, seat_id_flag = True):
    row_str = bp[:7]
    col_str = bp[7:]
    row_no = convert_to_bin(row_str, 'B', 'F')
    col_no = convert_to_bin(col_str, 'R', 'L')
    seat_id = (row_no * 8) + col_no

    if seat_id_flag:
        return seat_id
    else:
        return row_no, col_no


if __name__ == '__main__':

    max_seat_id = 0
    for bp in passes.readlines():
        bp = bp.strip()
        seat_id = seat_desc(bp)
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    print(max_seat_id)
    passes.close()
