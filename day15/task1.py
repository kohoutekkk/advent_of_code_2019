#numbers_str = '0,3,6' #test
numbers_str = '8,13,1,0,18,9' #task

#initiate
last_seen = {}
for loc, num in enumerate(numbers_str.split(',')[:-1]):
    last_seen[int(num)] = loc + 1

last_number = int(numbers_str.split(',')[-1])
starting_index = len(numbers_str.split(','))

print(last_seen, last_number)
print(starting_index)

for index in range(starting_index, 2020):

    if last_number in last_seen:
        new_number = index - last_seen[last_number]
        last_seen[last_number] = index
        last_number = new_number
    else:
        last_seen[last_number] = index
        last_number = 0

print(last_seen, last_number)

print(last_number)