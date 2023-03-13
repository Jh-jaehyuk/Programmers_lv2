from collections import Counter
def solution(clothes):
    count = Counter([clothes[i][1] for i in range(len(clothes))])
    answer = 1
    for i in list(count.values()):
        answer *= i+1
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
