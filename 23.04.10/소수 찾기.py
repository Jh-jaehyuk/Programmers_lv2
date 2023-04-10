from itertools import permutations


def is_prime_number(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    visited = [False] * 1000000
    l = [i for i in numbers]
    for i in range(1, len(numbers) + 1):
        arr = list(permutations(l, i))
        for j in arr:
            x = ''.join(j)
            if is_prime_number(int(x)) and not visited[int(x)]:
                answer += 1
                visited[int(x)] = True

    return answer


print(solution('011'))
