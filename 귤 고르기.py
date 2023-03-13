from collections import Counter
def solution(k, tangerine):
    count = 0
    answer = 0
    tangerine = Counter(tangerine)
    d = dict(tangerine.most_common())
    # dictionary 가 시간복잡도에서 리스트보다 유리함.
    if list(d.values())[0] >= k:
        return 1

    for _, i in d.items():
        count += i
        answer += 1
        if count >= k:
            break

    return answer

print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
