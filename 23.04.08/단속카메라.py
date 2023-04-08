def solution(routes):
    arr = sorted(routes, key=lambda x:x[1])
    x = arr[0][1]
    answer = 1

    for i in range(1, len(arr)):
        if x >= arr[i][0]:
            pass
        else:
            answer += 1
            x = arr[i][1]

    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
