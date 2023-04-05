import heapq

def solution(operations):
    answer = []
    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(answer, int(b))
        elif a == 'D':
            if answer:
                if b == '-1':
                    heapq.heappop(answer)
                else:
                    answer.sort()
                    del answer[-1]
    answer.sort()

    if answer:
        return [answer[-1], answer[0]]
    else:
        return [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
