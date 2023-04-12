def solution(p):

    def check(s):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            else:
                count -= 1

            if count < 0:
                return False
        else:
            return True

    def split_string(s):
        a = 0
        idx = 0
        for i in s:
            if i == '(':
                a += 1
            else:
                a -= 1
            idx += 1
            if a == 0:
                u = s[:idx]
                v = s[idx:]
                return u, v

    def change(s):
        arr = [i for i in s]
        arr.pop(0)
        arr.pop()
        new_s = ''
        if not s:
            return new_s

        else:
            for i in arr:
                if i == '(':
                    new_s += ')'
                else:
                    new_s += '('
        return new_s

    def recursive_string(s):
        if not s:
            return ''

        u, v = split_string(s)

        if check(u):
            return u + recursive_string(v)

        else:
            new_u = change(u)
            return '(' + recursive_string(v) + ')' + new_u

    return ''.join(recursive_string(p))


print(solution('(()())()()'))
