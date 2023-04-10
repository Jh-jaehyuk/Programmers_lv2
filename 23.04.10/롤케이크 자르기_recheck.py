# Counter 함수의 시간복잡도는 O(N)

from collections import Counter


def solution(topping):
    right = Counter(topping)
    left = set()
    count = 0

    for i in topping:
        right[i] -= 1

        if not right[i]:
            del right[i]

        left.add(i)

        if len(right) == len(left):
            count += 1

    return count


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
