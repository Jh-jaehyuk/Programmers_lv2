def solution(gems):
    answer = [0, len(gems)]
    length = len(set(gems))
    start = 0
    end = 0
    d = {gems[0] : 1}
    while start < len(gems) and end < len(gems):

        if len(d) == length:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                d[gems[start]] -= 1
                if not d[gems[start]]:
                    del d[gems[start]]
                start += 1

        else:
            end += 1

            if end == len(gems):
                break

            if gems[end] in d:
                d[gems[end]] += 1

            else:
                d[gems[end]] = 1

    return [answer[0] + 1, answer[1] + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
