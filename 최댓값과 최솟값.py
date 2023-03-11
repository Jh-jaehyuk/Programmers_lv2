def solution(s):
    int_s = [int(i) for i in s.split(' ')]
    answer = f'{min(int_s)} {max(int_s)}'
    return answer

print(solution('1 2 3 4'))
