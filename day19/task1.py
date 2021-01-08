#recursive solution

#rules, codes = open('data/test_rules.txt', 'r').read().split('\n\n')
rules, codes = open('data/rules.txt', 'r').read().split('\n\n')

codes_list = codes.split('\n')

rule_dict = {}
for rule in rules.split('\n'):
    rnum_str, rules_str = rule.split(': ')
    rule_dict[rnum_str] = rules_str

#print(rule_dict)

def use_rule(code, rule_num):
    #print(code, rule_num)
    rule = rule_dict[rule_num]
    if rule.startswith('"'): #endo of search for matching rule
        rule = rule[1:-1]
        if code.startswith(rule):
            return len(rule)
        else:
            return -1

    for possibility in rule.split(' | '):
        steps = 0
        for rule_num in possibility.split(' '):
            recursive_call_steps = use_rule(code[steps:], rule_num)
            if recursive_call_steps == -1:
                steps = -1
                break
            steps += recursive_call_steps
        if steps != -1:
            return steps
    return -1

matched_codes = 0
for cd in codes_list:
    if use_rule(cd, '0') == len(cd):
        matched_codes += 1
print(matched_codes)