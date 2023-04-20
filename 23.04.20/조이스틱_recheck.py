def solution(name):
    answer = 0

    min_val = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == "A":
            next_idx += 1

        min_val = min([min_val, 2 * i + len(name) - next_idx, i + 2 * (len(name) - next_idx)])

    answer += min_val

    return answer


print(solution("BCAABCDAAAAAAD"))
