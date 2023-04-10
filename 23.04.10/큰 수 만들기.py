def solution(number, k):
    stack = []

    for i in number:
        while stack and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)

    if k != 0:
        stack = stack[:(-1 * k)]

    return ''.join(stack)


print(solution('4321', 1))
