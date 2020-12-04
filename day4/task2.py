

#passports = open('data/test_passports2.txt', 'r')
passports = open('data/passports.txt', 'r')


def is_valid(pp):
    validity = True
    for key, value in pp.items():
        if key == 'byr':
            try:
                byr = int(value)
                if not (1920 <= byr <= 2002):
                    validity = False
                    #print(key)
            except:
                validity = False
                #print(key)
        if key == 'iyr':
            try:
                iyr = int(value)
                if not (2010 <= iyr <= 2020):
                    validity = False
                    #print(key)
            except:
                validity = False
                #print(key)
        if key == 'eyr':
            try:
                eyr = int(value)
                if not (2020 <= eyr <= 2030):
                    validity = False
                    #print(key)
            except:
                validity = False
                #print(key)
        if key == 'hgt':
            unit = value[-2:]
            val = value[:-2]
            #print(unit)
            #print(val)
            if unit == 'cm':
                try:
                    ht = int(val)
                    if not (150 <= ht <= 193):
                        validity = False
                        #print(key)
                except:
                    validity = False
                    #print(key)
            elif unit == 'in':
                try:
                    ht = int(val)
                    if not (59 <= ht <= 76):
                        validity = False
                        #print(key)
                except:
                    validity = False
                    #print(key)
            else:
                validity = False
                #print(key)
        if key == 'hcl':
            if value[0] != '#':
                validity = False
                #print(key)
            if len(value[1:]) != 6:
                validity = False
                #print(key)
            for i in value[1:]:
                if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                    validity = False
                    #print(key)

        if key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                validity = False
                #print(key)
        if key == 'pid':
            if not (value.isdecimal() and len(value) == 9):
                validity = False
                #print(key)
    return validity


required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
print(required_fields)
print('****')

pp_dict = {}
valid_passports = 0
for line in passports.readlines():
    # what to do at the end of a passport
    if line == '\n':
        keys_set = set(pp_dict.keys())
        print(pp_dict)
        # print(keys)
        # print('\n')
        print(is_valid(pp_dict))
        print(pp_dict)
        if (len(required_fields - keys_set) == 0) and is_valid(pp_dict):
            valid_passports += 1
        pp_dict = {}
    else:
        # what to do with regular passport line
        kv_pairs = line.split(' ')
        for item in kv_pairs:
            #print(item)
            if ':' in item:
                its = item.split(':')
                pp_dict[its[0].strip()] = its[1].strip()
            else:
                pp_dict[item] = '-1'

passports.close()

# one last run at the end of file
keys_set = set(pp_dict.keys())
print(is_valid(pp_dict))
print(pp_dict)
# print(keys)
if (len(required_fields - keys_set) == 0) and is_valid(pp_dict):
    valid_passports += 1

print(valid_passports)
