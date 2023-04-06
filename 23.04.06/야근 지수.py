import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    arr = []
    for i in works:
        heapq.heappush(arr, -i)

    while n > 0:
        heapq.heappush(arr, heapq.heappop(arr) + 1)
        n -= 1

    return sum([j * j for j in arr])
