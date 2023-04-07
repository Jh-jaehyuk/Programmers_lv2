def solution(skill, skill_trees):
    arr1 = list(skill)
    count = 0

    for i in skill_trees:
        arr2 = [j for j in list(i) if j in arr1]
        k = len(arr2)
        if arr2 == arr1[:k]:
            count += 1

    return count


print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))
