def solution(numbers):
    global check
    answer = []

    for number in numbers:
        bin_num = bin(number)[2:]
        p = 0

        while len(bin_num) >= 2 ** p:
            p += 1

        bin_num = bin_num.rjust((2 ** p) - 1, '0')
        mid = len(bin_num) // 2
        check = True
        dfs(mid, bin_num.count('1'), bin_num)
        answer.append(1 if check else 0)

    return answer


def dfs(idx, count, num):
    global check
    if count == 0:
        return

    if num[idx] == '0':
        check = False
        return

    left, right = num[:idx], num[(idx + 1):]

    dfs(idx // 2, left.count('1'), left)
    dfs(idx // 2, right.count('1'), right)


print(solution([7, 42, 5, 63, 111, 95]))
