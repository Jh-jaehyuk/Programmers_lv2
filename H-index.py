def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in citations:
        if len(citations) == 1:
            if i == 0:
                return 0
            else:
                return 1

        if i >= citations.index(i) + 1:
            print(i, citations.index(i) + 1, answer)
            answer += 1

    return answer
# https://www.ibric.org/myboard/read.php?Board=news&id=270333 참고
print(solution([3, 0, 6, 1, 5]))
