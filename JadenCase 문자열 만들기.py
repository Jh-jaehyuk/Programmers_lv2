def solution(s):
    l = s.split(' ')
    print(l)
    for i in range(len(l)):
        if l[i] == '':
            pass
        else:
            l[i] = l[i][0].upper() + l[i][1:].lower()
    return ' '.join(l)

print(solution("a  aa"))

