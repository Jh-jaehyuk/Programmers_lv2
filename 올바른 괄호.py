def solution(s):
    a = 0
    b = 0
    if s[0] == '(' and s[-1] == ')':
        for i in s:
            if i == '(':
                a += 1
            else:
                b += 1

            if b > a:
                return False
    else:
        return False
    return True if a-b == 0 else False

