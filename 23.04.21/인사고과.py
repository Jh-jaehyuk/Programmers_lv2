def solution(scores):
    answer = 1
    target = scores[0]
    target_s = sum(target)
    scores.sort(key=lambda x: (-x[0], x[1]))
    max_s1 = 0

    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1

        if max_s1 <= score[1]:
            if target_s < score[0] + score[1]:
                answer += 1
            max_s1 = score[1]

    return answer
