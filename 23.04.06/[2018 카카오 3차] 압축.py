import string


def solution(msg):
    d = dict()
    s = string.ascii_uppercase
    for i in range(1, 27):
        d[s[i - 1]] = i

    answer = []
    idx = 0
    length = 0
    max_idx = 26

    while True:
        length += 1
        if msg[idx:idx + length] not in d:
            max_idx += 1
            d[msg[idx:idx + length]] = max_idx
            answer.append(d[msg[idx:(idx + length - 1)]])
            idx = idx + length - 1
            length = 0
        else:
            if (idx + length - 1) == len(msg):
                answer.append(d[msg[idx:(idx + length - 1)]])
                break

    return answer

print(solution("ABABABABABABABAB"))
