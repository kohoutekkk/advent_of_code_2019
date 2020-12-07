#answers = open('data/test_answers.txt', 'r')
answers = open('data/answers.txt', 'r')

answer_sets = []
total_answers = 0
for answer in answers.readlines():

    if answer == '\n':
        unioun_of_sets = set()
        for aset in answer_sets:
            unioun_of_sets = unioun_of_sets.union(aset)
        total_answers += len(unioun_of_sets)
        answer_sets = []
    else:
        answer_sets.append(set(answer.strip()))

unioun_of_sets = set()
for aset in answer_sets:
    unioun_of_sets = unioun_of_sets.union(aset)
total_answers += len(unioun_of_sets)
print(total_answers)
answers.close()
