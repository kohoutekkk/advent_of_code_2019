from collections import deque

cipher_file = open('data/test_data.txt', 'r')
past_length = 5

cipher_file = open('data/data.txt', 'r')
past_length = 25

def is_sum(num, available):
    is_sum_bool = False
    for no in available:
        if (num - no) != no and (num - no) in available:
            is_sum_bool = True
            break
    return is_sum_bool

available_numbers = deque([])
for number_str in cipher_file.readlines():
    number = int(number_str.strip())

    if len(available_numbers) < past_length:
        available_numbers.append(number)
    else:
        if is_sum(number, available_numbers):
            _ = available_numbers.popleft()
            available_numbers.append(number)
        else:
            print(number)
            break


#cipher_file.close()