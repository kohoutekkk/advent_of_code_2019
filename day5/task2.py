from task1 import seat_desc


airplane = [int(row*8 + col) for row in range(128) for col in range(8)]
airplane_set = set(airplane)

#print(len(airplane))

passes = open('data/boarding_passes.txt', 'r')

#print(len([line for line in passes]))


if __name__ == '__main__':
    taken_seats = [int(seat_desc(bp)) for bp in passes.readlines()]
    taken_seats_set = set(taken_seats)

    possible = airplane_set - taken_seats_set

    my_seats = []
    for seat_id in possible:
        if ((seat_id + 1) in taken_seats) and ((seat_id -1) in taken_seats):
            my_seats.append(seat_id)

    #print(len(my_seats))
    print(my_seats)
#print(airplane_set - taken_seats_set)
passes.close()
