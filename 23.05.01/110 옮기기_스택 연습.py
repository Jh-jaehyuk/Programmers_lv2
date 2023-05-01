def check(s):
    count = 0
    stack = []

    for i in s:
        if i == '1':
            stack.append(i)
        else:
            if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                stack.pop()
                stack.pop()
                count += 1
            else:
                stack.append('0')

    x = ''.join(stack)
    for i in range(len(x) - 1, -1, -1):
        if x[i] == '0':
            tmp = x[:(i + 1)]
            tmp += '110' * count
            tmp += x[(i + 1):]
            break
    else:
        tmp = '110' * count
        tmp += x

    return tmp


def solution(s):
    answer = []
    for ss in s:
        answer.append(check(ss))

    return answer


print(solution(['1110', '100111100', '0111111010']))
