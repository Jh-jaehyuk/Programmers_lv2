def solution(numbers):
    if max(numbers) == 0:
        return '0'
    arr = [str(i) for i in numbers]
    arr = sorted(arr, key=lambda x:(x * 4), reverse=True)

    answer = ''.join(arr)
    return answer


print(solution([3, 33, 333, 334]))
