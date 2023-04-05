def solution(numbers, target):
    result = 0

    def dfs(start, count):
        nonlocal result
        if count == len(numbers):
            if start == target:
                result += 1
            return

        arr = [-start, start]
        if count == 1:
            for i in range(2):
                dfs(arr[i] + numbers[count], count + 1)
                dfs(arr[i] - numbers[count], count + 1)
        else:
            dfs(start + numbers[count], count + 1)
            dfs(start - numbers[count], count + 1)

    dfs(numbers[0], 1)
    return result

print(solution([4,1,2,1], 4))
