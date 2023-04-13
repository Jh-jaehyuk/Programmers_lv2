import re
from itertools import permutations


def solution(expression):
    answer = []
    combi = list(permutations(['+', '-', '*'], 3))

    for c in combi:
        num = re.split('[*+-]', expression)
        op = re.split('[0-9]+', expression)[1:-1] # 공백 제거용 슬라이싱

        for i in c:
            while i in op:
                idx = op.index(i)
                num[idx] = str(eval(num[idx] + i + num[idx + 1]))
                del num[idx + 1]
                del op[idx]
        answer.append(abs(int(num[0])))
    return max(answer)


print(solution('100-200*300-500+20'))
