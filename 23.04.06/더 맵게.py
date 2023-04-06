import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        x = heapq.heappop(scoville)
        if x >= K:
            return answer
        y = heapq.heappop(scoville)

        heapq.heappush(scoville, x + y * 2)
        answer += 1

    if scoville[0] <= K:
        return -1
    else:
        return answer

print(solution([7,8,9,10,12], 7))
