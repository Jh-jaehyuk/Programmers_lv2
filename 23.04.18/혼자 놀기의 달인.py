def solution(cards):
    answer = 0

    for i in range(len(cards)):
        visited = [False] * (len(cards) + 1)
        queue = [cards[i]]
        visited[i + 1] = True
        while len(queue) < len(cards):
            if not visited[queue[-1]]:
                visited[queue[-1]] = True
                queue.append(cards[queue[-1] - 1])
            else:
                break

        x = len(queue)

        for j in range(len(cards)):
            visited_copy = visited[:]
            if visited_copy[j + 1]:
                continue

            queue2 = [cards[j]]
            visited_copy[j + 1] = True

            while len(queue2) < len(cards):
                if not visited_copy[queue2[-1]]:
                    visited_copy[queue2[-1]] = True
                    queue2.append(cards[queue2[-1] - 1])
                else:
                    break

            y = len(queue2)

            answer = max(answer, x * y)

    return answer


print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
