def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)

        else:
            x = bin(i)[2:]
            x = '0' + x
            idx = x.rfind('0')
            x = list(x)
            x[idx] = '1'
            x[idx + 1] = '0'
            y = ''.join(x)
            answer.append(int(y, 2))

    return answer


print(solution([2, 7]))
