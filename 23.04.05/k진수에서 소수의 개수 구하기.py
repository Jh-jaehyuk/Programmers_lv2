def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    result = 0
    rev_base = ''
    if k != 10:
        while n > 0:
            n, mod = divmod(n, k)
            rev_base += str(mod)
        rev_base = rev_base[::-1]
    else:
        rev_base = str(n)

    tmp = ''
    for i in rev_base:
        if i == '0':
            if tmp and is_prime_number(int(tmp)):
                result += 1
            tmp = ''
        else:
            tmp += i

    if tmp and is_prime_number(int(tmp)):
        result += 1

    return result
