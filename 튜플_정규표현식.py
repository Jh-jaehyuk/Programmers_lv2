import re
def solution(s):
    answer = []
    print(re.findall('\d+', s)) # s 안에서 정수만 추출하는 정규표현식
    s = s[:-2].replace('{', '').replace(',', ' ').split('}')
    s = [i.split() for i in s]
    s.sort(key=lambda x:len(x)) # 길이가 짧은것에서 긴 순서로

    for i in s:
        d = set(i) - set(answer)
        answer.append(list(d)[0])
    answer = list(map(int, answer))

    return answer

print(solution("{{20,111},{111}}"))
