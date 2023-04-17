def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for i in range(1, (len(s) // 2) + 1):
        x = ''
        count = 1
        tmp = s[:i]

        for j in range(i, len(s), i):
            if tmp == s[j:(i + j)]:
                count += 1

            else:
                if count != 1:
                    x += str(count)
                x += tmp
                tmp = s[j:(j + i)]
                count = 1

        if count != 1:
            x += str(count)
        x += tmp

        answer.append(len(x))

    return min(answer)


print(solution("abcabcdede"))
