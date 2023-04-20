import heapq


def solution(n, k, enemy):
    answer = 0
    heap = []

    for i in enemy:
        heapq.heappush(heap, -i)
        if k == 0 and n < i:
            break
        if k != 0 and n < i:
            n += -1 * heapq.heappop(heap)
            k -= 1

        n -= i
        answer += 1

    return answer


print(solution(2, 4, [4, 2, 4, 5, 3, 3, 1]))
