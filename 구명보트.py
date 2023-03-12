from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    dq = deque(people)
    while len(dq) > 1:
        if dq[0] + dq[-1] <= limit:
            # 최소 몸무게와 최대 몸무게의 합이 limit 보다 작은게 가장 좋은 조건.
            dq.popleft()
        answer += 1
        dq.pop()
    if dq:
        answer += 1
    return answer

print(solution([70,50,80,50], 100))
