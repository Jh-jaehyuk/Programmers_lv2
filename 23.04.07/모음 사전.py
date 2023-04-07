from itertools import product


def solution(word):
    arr = []
    for i in range(5):
        for j in product('AEIOU', repeat=(i + 1)):
            arr.append(''.join(j))
    arr.sort()
    return arr.index(word) + 1
