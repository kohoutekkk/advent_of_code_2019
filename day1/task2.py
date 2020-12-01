from typing import List

numbers_file = open("data/numbers.txt", "r")
numbers_list = []
for line in numbers_file.readlines():
    numbers_list.append(int(line))

def find_triplet(numbers: List[int] = None, expected_sum: int = 2020):
    n1 = None
    n2 = None
    n3 = None

    for i in numbers:
        for j in numbers:
            if (expected_sum - i -j) in numbers:
                n1 = i
                n2 = j
                n3 = expected_sum - i -j
                break
    return n1 * n2 * n3


if __name__ == '__main__':
    print(find_triplet(numbers_list))