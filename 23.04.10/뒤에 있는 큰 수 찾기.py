import heapq


def solution(numbers):
    answer = [-1] * len(numbers)
    arr = []

    for i in range(len(numbers)):
        val = numbers[i]

        while arr and arr[0][0] < val:
            _, idx = heapq.heappop(arr)
            answer[idx] = val

        heapq.heappush(arr, [val, i])

    return answer


print(solution([9, 1, 5, 3, 6, 2]))
