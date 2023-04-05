from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    count = 1

    if location == 0 and queue[location] == max(queue):
        return 1

    while queue:
        max_q = max(queue)
        if queue[0] == max_q:
            queue.popleft()
            count += 1

        else:
            queue.rotate(-1)

        location -= 1
        if location < 0:
            location = len(queue) - 1

        if location == 0 and queue[location] == max(queue):
            return count

    return len(priorities)

print(solution([1,1,1,1,1], 0))
