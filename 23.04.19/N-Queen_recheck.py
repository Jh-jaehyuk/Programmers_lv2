# 1차원 배열로 접근하는 건 상상도 못함...

def solution(n):

    def check(x, y, col):
        for i in range(x):
            if col[i] == y or abs(y - col[i]) == abs(x - i):
                return False
        return True

    def queen(x, n, col):
        if x == n:
            return 1
        count = 0

        for y in range(n):
            if check(x, y, col):
                col[x] = y
                count += queen(x + 1, n, col)

        return count

    col = [0] * n
    return queen(0, n, col)
