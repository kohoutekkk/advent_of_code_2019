from collections import deque

cipher_file = open('data/data.txt', 'r')
required_sum = 756008079

#cipher_file = open('data/test_data.txt', 'r')
#required_sum = 127

available_numbers = deque([])
for number_str in cipher_file.readlines():
    number = int(number_str.strip())
    available_numbers.append(number)

    if sum(available_numbers) == required_sum:
        break

    if sum(available_numbers) < required_sum:
        continue
    else:
        while sum(available_numbers) > required_sum:
            _ = available_numbers.popleft()

        if sum(available_numbers) == required_sum:
            break

print(min(available_numbers) + max(available_numbers))