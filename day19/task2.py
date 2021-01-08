#recursive solution

#rules, codes = open('data/test_rules_2.txt', 'r').read().split('\n\n')
rules, codes = open('data/rules.txt', 'r').read().split('\n\n')

codes_list = codes.split('\n')

rule_dict = {}
for rule in rules.split('\n'):
    rnum_str, rules_str = rule.split(': ')
    rule_dict[rnum_str] = rules_str

rule_dict['8'] = '42 | 42 8'
rule_dict['11'] = '42 31 | 42 11 31'

print(rule_dict)

def use_rule(code, rule_num):
    print(code, rule_num)
    rule = rule_dict[rule_num]
    if rule.startswith('"'): #endo of search for matching rule
        rule = rule[1:-1]
        if code.startswith(rule):
            return [len(rule)]
        else:
            return []

    possible_matches = []
    for possibility in rule.split(' | '):
        steps = [0]
        for rule_num in possibility.split(' '):
            rule_steps = []
            for step in steps:
                recursive_call_steps = use_rule(code[step:], rule_num)
                for rcs in recursive_call_steps:
                    rule_steps.append(rcs + step)
            steps = rule_steps
        possible_matches += steps

    return possible_matches


matched_codes = 0

for cd in codes_list:
    if len(cd) in use_rule(cd, '0'):
        matched_codes += 1
print(matched_codes)
