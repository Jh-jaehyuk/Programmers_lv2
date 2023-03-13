def solution(s):
    answer = 0
    for i in range(len(s)):
        ss = s[i:] + s[:i] # s를 회전 시킴
        while True:
            temp = ss
            print(temp)
            # 올바른 괄호가 하나라도 있으면 올바른 괄호 제거.
            if '()' in ss:
                ss = ss.replace('()', '')
            elif '{}' in ss:
                ss = ss.replace('{}', '')
            elif '[]' in ss:
                ss = ss.replace('[]', '')
            # 올바른 괄호가 하나도 없으면 반복문을 벗어나서 s 회전시킴.
            if temp == ss:
                break
        # 올바른 괄호가 다 지워져서 하나도 남지 않으면 정답 + 1
        if ss == '':
            answer += 1
    return answer

print(solution("[](){}"))
