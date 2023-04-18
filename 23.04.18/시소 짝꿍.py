from collections import Counter


def solution(weights):
    answer = 0
    c = Counter(weights)

    for i in c.values():
        # weights 안에 중복되는 원소가 있는 경우
        if i > 1:
            answer += (i * (i - 1)) // 2
    # 중복되는 원소에 대해 앞에서 처리했기 때문에 중복 원소 제거
    weights = list(set(weights))
    # weight에 있는 원소들에 대해서
    for weight in weights:
        # weight에 각각 3/4, 2/3, 2/4를 곱해보고
        for j in [3 / 4, 2 / 3, 2 / 4]:
            # 그 값이 weights 리스트 안에 있다면
            if weight * j in weights:
                # weight 가 나온 횟수와 weight 에 j를 곱해준 값이 나온 횟수를 곱하여 더해줌.
                answer += c[weight] * c[weight * j]

    return answer


print(solution([100, 180, 360, 100, 270]))
