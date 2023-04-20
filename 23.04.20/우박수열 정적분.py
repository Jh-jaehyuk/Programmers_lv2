def solution(k, ranges):
    answer = []
    arr = []
    square = []
    idx = 0
    while k >= 1:
        arr.append((idx, k))
        if k == 1:
            break
        idx += 1
        if k % 2 == 0:
            k //= 2
        else:
            k *= 3
            k += 1

    for i in range(len(arr) - 1):
        square.append((arr[i][1] + arr[i + 1][1]) / 2)

    for r in ranges:
        s = 0
        a, b = r
        b = len(square) + b
        if a > b:
            answer.append(-1)
        else:
            for k in range(a, b):
                s += square[k]
            answer.append(s)

    return answer


print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))
