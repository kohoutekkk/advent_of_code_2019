from typing import List

numbers_file = open("data/numbers.txt", "r")
numbers_list = []
for line in numbers_file.readlines():
    numbers_list.append(int(line))


def find_pair(numbers: List[int] = None, expected_sum: int = 2020):
    n1 = None
    n2 = None
    for i in numbers:
        if (expected_sum - i) in numbers:
            n1 = i
            n2 = expected_sum - i
            break
    return n1 * n2


if __name__ == '__main__':
    print(find_pair(numbers_list))
