#ticket_info_file = open('data/test_tickets.txt','r')
ticket_info_file = open('data/tickets.txt','r')



# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
my_ticket_flag = False
nearby_tickets_flag = False
description_and_values = {}
all_values = set()
scanning_error_rate = 0

def process_ticket_info(line):
    description, numbers = line.strip().split(':')
    ranges_list = numbers.split('or')
    accepted_values = set([])
    for rang in ranges_list:
        lower_b, upper_b = rang.strip().split('-')
        av = set(range(int(lower_b), int(upper_b) + 1))
        accepted_values = accepted_values.union(av)
    return description, accepted_values

def process_my_ticket(line):
   ...

def process_nearby(line):
    if line.strip() == '' or line.strip() == 'nearby tickets:':
        return 0
    else:
        numbers = [int(number) for number in line.strip().split(',')]
        ser = 0
        for number in numbers:
            if number not in all_values:
                ser += number
        return ser



for line in ticket_info_file.readlines():
    #print(my_ticket_flag)
    #print(line.strip() == "")
    #print(line)
    if my_ticket_flag and line.strip() == "":
        #print('hello')
        nearby_tickets_flag = True

    if not my_ticket_flag and line.strip() == "":
        my_ticket_flag = True

    if not my_ticket_flag and not nearby_tickets_flag:
        description, accepted_values = process_ticket_info(line)
        description_and_values[description] = accepted_values
        all_values = all_values.union(accepted_values)

    elif my_ticket_flag and not nearby_tickets_flag:

        process_my_ticket(line)
    else:

        local_ser = process_nearby(line)
        scanning_error_rate += local_ser

print(scanning_error_rate)