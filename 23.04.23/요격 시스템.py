def solution(targets):
    answer = 0

    targets.sort(key=lambda x:(x[1], x[0]))
    end = 0
    for target in targets:
        s, e = target

        if end <= s:
            answer += 1
            end = e

    return answer


print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))
