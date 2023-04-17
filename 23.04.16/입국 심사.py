def solution(n, times):
    answer = min(times) * n
    left = 0
    right = min(times) * n

    def check(time):
        count = 0
        for i in times:
            count += time // i
        return count

    while left <= right:
        mid = (left + right) // 2
        if check(mid) >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
