from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))
    print(combi)

    arr = []
    for c in combi:
        tmp = [tuple(item[key] for key in c) for item in relation]
        if len(set(tmp)) == row:
            check = True

            for x in arr:
                if set(x).issubset(set(c)):
                    check = False
                    break

            if check:
                arr.append(c)

    return len(arr)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
