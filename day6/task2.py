import functools

#answers = open('data/test_answers.txt', 'r')
answers = open('data/answers.txt', 'r')

answer_sets = []
total_answers = 0
for answer in answers.readlines():
    if answer == '\n':
        all_true = functools.reduce(lambda a,b: a.intersection(b), answer_sets)
        total_answers += len(all_true)
        answer_sets = []
    else:
        answer_sets.append(set(answer.strip()))

all_true = functools.reduce(lambda a,b: a.intersection(b), answer_sets)
total_answers += len(all_true)
print(total_answers)
answers.close()
