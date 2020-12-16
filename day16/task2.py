import numpy as np

#ticket_info_file = open('data/test_tickets2.txt', 'r')
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
tickets_list = []

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
    return [int(number) for number in line.strip().split(',')]

def process_nearby(line):
    if line.strip() == '' or line.strip() == 'nearby tickets:':
        return None
    else:
        numbers = [int(number) for number in line.strip().split(',')]
        match = True
        for number in numbers:
            if number not in all_values:
                match = False
        if match:
            return numbers




for line in ticket_info_file.readlines():
    #print(my_ticket_flag)
    #print(line.strip() == "")
    #print(line)
    if line.strip() == 'your ticket:':
        continue
    if my_ticket_flag and line.strip() == "":
        #print('hello')
        nearby_tickets_flag = True
        continue

    if not my_ticket_flag and line.strip() == "":
        my_ticket_flag = True
        continue

    if not my_ticket_flag and not nearby_tickets_flag:
        description, accepted_values = process_ticket_info(line)
        description_and_values[description] = accepted_values
        all_values = all_values.union(accepted_values)

    elif my_ticket_flag and not nearby_tickets_flag:
        my_ticket = process_my_ticket(line)

    else:
        line_result = process_nearby(line)
        if line_result:
            tickets_list.append(line_result)

tickets_array = np.array(tickets_list)

index_dict = {}

empty_keys = list(description_and_values.keys())
available_indexes = list(range(tickets_array.shape[1]))

while empty_keys:
    print(f'ek:{len(empty_keys)}')

    for ind in range(tickets_array.shape[1]):
        relevant_col = set(tickets_array[:,ind])
        #print('-'*40)
        #print(relevant_col)
        valid_keys = []
        for key in empty_keys:
            values = description_and_values[key]
            #print(values)
            #print(relevant_col.intersection(values))
            #print(relevant_col == relevant_col.intersection(values))

            if relevant_col == relevant_col.intersection(values):
                valid_keys.append(key)
        print(f'ind {ind}')
        print(f'vk: {len(valid_keys)}')
        if len(valid_keys) == 1:
            index_dict[valid_keys[0]] = ind
            empty_keys.remove(valid_keys[0])
            available_indexes.remove(ind)



print(index_dict)
mult_dep = 1

for key, value in index_dict.items():
    if 'departure' in key:
        mult_dep *= my_ticket[value]

print(mult_dep)



#print(description_and_values)