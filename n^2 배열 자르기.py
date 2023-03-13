from itertools import chain # 2차원 배열을 1차원으로
def solution(n, left, right):
    answer = []
    i = left
    while i <= right:
        answer.append(max(i // n, i % n) + 1)
        # 1차원 배열의 인덱스 i를 2차원 배열 n x n의 크기 n으로 나눈 몫이
        # 2차원 배열의 x, 나머지가 y가 됨 i => (x, y) = (i // n, i % n)
        i += 1
    return answer

print(solution(3, 2 ,5))
