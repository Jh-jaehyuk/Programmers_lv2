def solution(n):
    i = n+1
    while True:
        if bin(n)[2:].count('1') == bin(i)[2:].count('1'):
            return i
        else:
            i += 1

print(solution(15))
