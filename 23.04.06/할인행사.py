def solution(want, number, discount):
    arr = []
    answer = 0
    for i in range(len(want)):
        for _ in range(number[i]):
            arr.append(want[i])
    arr.sort()

    for j in range(len(discount) - 9):
        arr2 = sorted(discount[j:j + 10])
        if arr == arr2:
            answer += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3,2,2,2,1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
