passports = open('data/test_passports2.txt', 'r')
#passports = open('data/passports.txt', 'r')

required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
print(required_fields)
print('****')

keys = []
valid_passports = 0
for line in passports.readlines():
    # what to do at the end of a passport
    if line == '\n':
        keys_set = set(keys)
        #print(keys)
        #print('\n')
        if len(required_fields - keys_set) == 0:
            valid_passports += 1
        keys = []
    else:
        # what to do with regular passport line
        kv_pairs = line.split(' ')
        keys = keys + [item.split(':')[0].strip() for item in kv_pairs]
passports.close()

#one last run at the end of file
keys_set = set(keys)
#print(keys)
if len(required_fields - keys_set) == 0:
    valid_passports += 1

print(valid_passports)
