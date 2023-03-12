def solution(s):
    # s = [i for i in s]
    # i = 0
    # while i <= len(s) - 2:
    #     if s[i] == s[i+1]:
    #         del s[i:i+2]
    #         if i > 0:
    #             i = i-1
    #         else:
    #             i = 0
    #     else:
    #         i += 1
    #
    # return 1 if len(s) == 0 else 0

    # 효율성 테스트에서 stack을 이용하지 않으면 통과되지 못함.
    answer = 0
    l = []
    for i in s:
        if len(l) == 0:
            l.append(i)
        else:
            if l[-1] == i:
                del l[-1] # del이 pop보다 미세하게 더 빠름.
            else:
                l.append(i)

    if len(l) == 0:
        answer = 1
    return answer

print(solution('baabaa'))
