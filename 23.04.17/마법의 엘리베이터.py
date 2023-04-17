def solution(storey):
    answer = 0
    while storey > 0:
        storey, mod = divmod(storey, 10)

        if mod > 5:
            answer += 10 - mod
            storey += 1
        elif mod == 5:
            if storey % 10 >= 5:
                answer += 10 - mod
                storey += 1
            else:
                answer += mod
        else:
            answer += mod

    return answer


print(solution(555))
